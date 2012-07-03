Name: rpm-macros-erlang
Version: 0.7.0
Release: alt1
Summary: RPM helper macros to rebuild erlang packages
License: %gpl3plus
Group: Development/Erlang
Source0: erlang.rpm.macros
Source1: erlang.rpm.env
BuildArch: noarch
Requires: rpm >= 4.0.4-alt78
Conflicts: rpm-build-erlang < 0.6.2-alt2
Packager: Led <led@altlinux.ru>
AutoReq: no

BuildRequires(pre): rpm-build-licenses

%description
These helper macros provide possibility to rebuild erlang modules by
some Alt Linux Team Policy compatible way.


%install
install -d -m 0755 %buildroot%_rpmmacrosdir
install -m 0644 %SOURCE0 %buildroot%_rpmmacrosdir/erlang
install -m 0644 %SOURCE1 %buildroot%_rpmmacrosdir/erlang.env


%files
%_rpmmacrosdir/*


%changelog
* Fri Feb 27 2009 Led <led@altlinux.ru> 0.7.0-alt1
- added macros for native and debug modules dirs

* Thu Feb 12 2009 Led <led@altlinux.ru> 0.6.2-alt3
- fixed Conflicts

* Wed Jan 14 2009 Led <led@altlinux.ru> 0.6.2-alt2
- initial build of separate rpm-macros-erlang

* Sun Sep 21 2008 Led <led@altlinux.ru> 0.6.2-alt1
- updated Requires
- cleaned up erlang.prov.files, erlang.env

* Wed Sep 10 2008 Led <led@altlinux.ru> 0.6.1-alt1
- yet another hack to erlang.prov.files for old buggy file(1)

* Wed Aug 20 2008 Led <led@altlinux.ru> 0.6.0-alt1
- remade erlang.prov.files

* Fri Aug 15 2008 Led <led@altlinux.ru> 0.5.0-alt1
- renamed rpm_req to erlang_req again
- cleaned up erlang.req
- updated BuildRequires

* Tue Jul 29 2008 Led <led@altlinux.ru> 0.4.1-alt1
- added hipe_bifs to default _erlang_req_modules_skiplist

* Wed Jul 23 2008 Led <led@altlinux.ru> 0.4.0-alt1
- renamed erlang_req to rpm_req
- updated erlang.req for compile rpm_req
- cleaned up Requires and BuildRequires

* Wed Jul 23 2008 Led <led@altlinux.ru> 0.3.6-alt1
- fixed/updated %%_sysconfdir/rpm/macros.d/erlang

* Fri Jul 11 2008 Led <led@altlinux.ru> 0.3.5-alt1
- improved erlang.{prov,req}.files

* Thu Jul 03 2008 Led <led@altlinux.ru> 0.3.4-alt1
- fixed erlang.prov.files

* Mon Jun 23 2008 Led <led@altlinux.ru> 0.3.3-alt1
- increased speed of searching requires

* Sun Jun 22 2008 Led <led@altlinux.ru> 0.3.2-alt1
- support environment variable for skip require modules

* Thu Jun 19 2008 Led <led@altlinux.ru> 0.3.1-alt1
- search requires only for files in %%_otplibdir/*/ebin/

* Thu Jun 19 2008 Led <led@altlinux.ru> 0.3-alt1
- simplified provedes and requires format

* Tue Feb 26 2008 Led <led@altlinux.ru> 0.2.1-alt1
- added warnings to erlang_req

* Mon Feb 25 2008 Led <led@altlinux.ru> 0.2-alt1
- 0.2:
  + fixed app-requires searching

* Sat Feb 23 2008 Led <led@altlinux.ru> 0.1-alt1
- initial build
