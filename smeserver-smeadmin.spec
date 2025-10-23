# $Id: smeserver-smeadmin.spec,v 1.17 2019/12/07 04:05:41 jpp Exp $
# Authority: vip-ire
# Name: Daniel Berteaud
# 

Summary: A graphical monitor, alert raising, and services supervision tool for your SME Server.
%define name smeserver-smeadmin
Name: %{name}
%define version 1.6
%define release 19
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.xz

BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch

BuildRequires: e-smith-devtools
BuildRequires: gettext

Requires: e-smith-base
Requires: smeserver-release >= 10
Requires: rrdtool-perl
Requires: rrdtool
Requires: hddtemp
Requires: sysstat
Requires: lm_sensors
Requires: perl-DBD-mysql
#Obsoletes: smeserver-sme8admin

AutoReqProv: no
%description
The main part of smeadmin is a daemon which gathers informations from logs
and other tools like systat, it then feed a mysql database and create RRD
graphs about your system state.
This daemon can also send periodics mails (with some logs), and alerts mails
based on configurable thresolds.

A panel is also available in the server-manager, with which you can access gathered
data, display the RRD graphs and configure the service.

This contrib is a bit inspired by e-smith-sysmon from Shad Lords.

%prep
%setup

%build
perl createlinks
%{__mkdir_p} root/etc/e-smith/web/panels/manager/html/smeadmin
%{__mkdir_p} root/usr/share/locale/en_US/LC_MESSAGES

xgettext --from-code UTF-8 -F --no-wrap -L perl \
        -o root/usr/share/locale/en_US/LC_MESSAGES/smeadmin.po \
        root/etc/e-smith/web/functions/smeadmin \
        root/usr/bin/smeadmind

/sbin/e-smith/generate-lexicons

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
--file /usr/bin/smeadmind 'attr(755,root,root)' \
--file /usr/share/doc/smeserver-smeadmin/add_ds_to_rrd.pl 'attr(755,root,root)' \
 > %{name}-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%changelog
* Thu Oct 23 2025 Vasarhelyi Zsolt <zsoltv@koozali.org> 1.6-19.sme
- Add requires perl-DBD-mysql [SME: 12961]

* Thu Oct 23 2025 Vasarhelyi Zsolt <zsoltv@koozali.org> 1.6-18.sme
- Fix database creation script [SME: 12961]

* Wed Oct 08 2025 Brian Read <brianr@koozali.org> 1.6-17.sme
- Apply change from startform to start_form and endform to end_form to CGI panels [SME: 12787]
- fix .gitignore and delete tarball from git repo [SME: 12787]

* Sat Sep 07 2024 cvs2git.sh aka Brian Read <brianr@koozali.org> 1.6-15.sme
- Roll up patches and move to git repo [SME: 12338]

* Sat Sep 07 2024 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.

* Fri Sep 06 2024 Terry Fage <terry@fage.id.au> 1.6-14.sme
- apply locale 2024-09-06.patch

* Sun May 19 2024 Jean-Philippe Pialasse <jpp@koozali.org> 1.6-13.sme
- fix pppoe not loging [SME: 12684]
  increase db volume field. filter display to last 24 months
  display in GB/MB instead of GiB/kiB

* Fri Dec 22 2023 Jean-Philippe Pialasse <tests@pialasse.com> 1.6-12.sme
- add accounting of auth_failed [SME: 12447]
  adding php8* services
- fix translation, reworked [SME: 10244]

* Fri Nov 11 2022 Jean-Philippe Pialasse <tests@pialasse.com> 1.6-10.sme
- apply locale 2022-11-11 patch

* Sun Sep 18 2022 Jean-Philippe Pialasse <tests@pialasse.com> 1.6-9.sme
- fix misisng stopped services [SME: 11643]

* Sat Jul 30 2022 Brian Read <brianr@bjsystems.co.uk> 1.6-8.sme
- Re-build and link to latest devtools [SME: 11997]

* Fri Jul 29 2022 Jean-Philippe Pialasse <tests@pialasse.com> 1.6-7.sme
- apply translation 2022-07-29
- add to core backup [SME: 12023]

* Mon Jul 18 2022 zsolt vasarhelyi <vasarhelyizsolt@hotmail.com> 1.6-6.sme
- bz11642 authproxy errorlog [SME: 11642]
- bz11590 error log [SME: 11590]

* Mon Jul 18 2022 Michel Begue <mab974@misouk.com> 1.6-5.sme
- get real ssh port from configuration db. [SME: 10761]

* Wed Sep 08 2021 Terry Fage <terry.fage@gmail.com> 1.6-4.sme
- apply locale 2021-09-08 patch

* Tue Aug 24 2021 Terry Fage <terry.fage@gmail.com> 1.6-3.sme
- apply locale 2021-08-24 patch

* Thu Mar 25 2021 Jean-Philippe Pialasse <tests@pialasse.com> 1.6-2.sme
- Re-build and link to latest devtools mysql not migrating sme9admind  [SME: 11062]
- Re-build and link to latest devtools config db sme9admind not migrated to smeadmind
- Re-build and link to latest devtools /var/lib/sme9admin not migrated
- add smeserver-smeadmin-update event
- Re-build and link to latest devtools services diplayed multiple times [SME: 11455]
- systemd unit
- review new logs locations
- check calls to sysvinit
- TODO implement new VPNs stats

* Thu Oct 15 2020 Brian Read <brianr@bjsystems.co.uk> 1.6-1
- Move to SME10, rename to smeadmin [SME: 11040, 11062]

* Sat Dec 07 2019 SME Translation Server <translations@contribs.org> 1.5-30.sme
- apply locale 2019-12-07 patch

* Mon Sep 09 2019 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-29.sme
- Re-build and link to latest devtools smeadmind die on mysql connection error [SME: 7683]

* Sat Dec 02 2017 SME Translation Server <translations@contribs.org> 1.5-28.sme
- apply locale 2017-12-02 patch

* Mon Aug 14 2017 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-27.sme
- add support for altqmail [SME: 10409]

* Mon Jul 10 2017 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-26.sme
- Re-build and link to latest devtools error after migrating sme8admin db, unable to access mysql db [SME: 10181]

* Sat Mar 25 2017 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-25.sme
- apply locale 2017-03-26 patch

* Wed Feb 01 2017 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-24.sme
- apply locale 2017-02-02.patch

* Sun Jan 01 2017 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-23.sme
- Re-build and link to latest devtools warning related to raid detection code [SME: 9886]
- Re-build and link to latest devtools warning related to non existing services removed sinces previous versions [SME: 9889]

* Tue Dec 20 2016 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-22.sme
- make CGI and pictures utf8 compliant [SME: 9894]
- apply smeserver-smeadmin-1.5-locale-2016-12-20.patch

* Sat Dec 17 2016 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-21.sme
- locals smeserver-smeadmin-1.5-locale-2016-12-18.patch

* Sat Dec 17 2016 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-20.sme
- Re-build and link to latest devtools last patch by adding path to called programs

* Thu Dec 15 2016 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-19.sme
- Re-build and link to latest devtools bad accounting for incoming and outgoing mail [SME: 8818]
- mail_in alert now account for all queued emails from qpsmtpd and sqpsmtpd
- mail_out alert now account for qmail total remote delivery attempts
- known issue : on first run will account more than 5 minutes ( whole log) and will alert for exceeding amount
- added accounting of qpsmtpd and sqpsmtpd code
- TODO: alert on qmail queue too high, alert on too many qpsmtpd connections

* Wed Nov 23 2016 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-18.sme
- Re-build and link to latest devtools limited size in mysql fields for traffic accounting [SME: 8399]

* Wed Nov 23 2016 Jean-Philippe Pialasse <tests@pialasse.com> 1.5-16.sme
- add more verbose email alert [SME: 9725]

* Fri Aug 21 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 1.5-15.sme
- Initial release to contribs9

* Wed Dec 24 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.5-14.sme
- changed  $mypid = `cat $mypid` by open(FIC,"<$mypid") [SME:8740]

* Tue Dec 23 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.5-13.sme
- Corrected bug of empty pids [SME:8732]
- Added exeption if the server is not in server & gateway [SME:8739]

* Thu Dec 11 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.5-12.sme
- corrected the dhcpd lease not reported  [SME:8724]

* Tue Nov 25 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.5-11.sme
- Added a restart to smeadmind when settings are changed in the smeadmin panel

* Sat Nov 22 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.5-10.sme
- added a second fan speed sensors
- added four HD TEMP sensors
- added a new graph only for hd temperature sensor
- added an event smeadmin-update for avoiding to restart the server
- added a tab to check the raid status 

* Sun Nov 16 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.5-9.sme
- Changed in smeadmind L937 °C in .{1,2} .... Thanks JPP

* Fri Nov 14 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.5-8.sme
- Added a service in rc7.d for lm_sensors
- added to sadf the -S to collect swap data
- changed txbyt/rxbyt to rxkB/txkB for collecting network load

* Mon Sep 01 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.5-7.sme
- added 755 to /usr/bin/smeadmind

* Wed Jun 18 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.5-6.sme
- Initial release to sme9

* Sun Dec 15 2013 Jean-Philippe Pialasse <tests@pialasse.com> 1.3-4.sme
- Re-build and link to latest devtools obsolete missing [SME: 7109]
- Re-build and link to latest devtools pppoe and vpn loging [SME: 8061]
- added monthly ppoe log  
- Re-build and link to latest devtools stop on mysql error too many connections [SME: 7683]  

* Sun Sep 09 2012 Jean-Philippe Pialasse <tests@pialasse.com> 1.3-3.sme
- startup fix [SME 3022]

* Wed Aug 15 2012 Jean-Philippe Pialasse <tests@pialasse.com> 1.3-2.sme
- 64 bits [SME 7040]

* Sun Jun 10 2012 Jean-Philippe Pialasse <tests@pialasse.com> 1.3-1.sme
- Initial version

