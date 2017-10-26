Name: rpm-build-erlang
Version: 0.7.10.1
Release: alt1
Summary: RPM helper scripts to calculate Erlang dependencies
License: %gpl3plus
Group: Development/Erlang
Source: %name-%version.tar
BuildArch: noarch
Requires: rpm >= 4.0.4-alt78
Requires: file >= 4.26
Requires: rpm-macros-erlang >= 0.6.2
AutoReq: yes, noerlang
Packager: Sergey Shilov <hsv@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: erlang-otp-devel

%description
These herlper scripts will look at Erlang modules (*.beam) and apps
(*.app) in your package, and will use this information to generate
automatic Requires and Provides tags for the package.


%prep
%setup


%build
mkdir ebin
erlc -W +inline -o ebin src/*.erl


%install
install -d -m 0755 %buildroot%_rpmlibdir
install -m 0644 ebin/* %buildroot%_rpmlibdir/
install -m 0755 erlang.* %buildroot%_rpmlibdir/


%files
%_rpmlibdir/*


%changelog
* Sun Nov 26 2017 Denis Medvedev <nbr@altlinux.org> 0.7.10.1-alt1
- finding app in ez files

* Sun Nov 26 2017 Denis Medvedev <nbr@altlinux.org> 0.7.10.0-alt1
- debugged version

* Mon Oct 23 2017 Denis Medvedev <nbr@altlinux.org> 0.7.0.6-alt1
- fixes buggy ez files detection.

* Thu Jul 28 2011 Sergey Shilov <hsv@altlinux.org> 0.7.0.3-alt1
- fix buggy erlang.prov.files result if *.app is ASCII text, with very long lines.

* Sun Mar 20 2011 Sergey Shilov <hsv@altlinux.org> 0.7.0.2-alt2
- fix packager;
- fix BuildRequires: erlang -> erlang-otp-devel
- rebuild with Erlang R14B02

* Tue Jan 12 2010 Led <led@altlinux.ru> 0.7.0.2-alt1
- 0.7.0.2:
  + fixed erlang.prov script

* Thu Feb 12 2009 Led <led@altlinux.ru> 0.7.0.1-alt1
- 0.7.0.1:
  + erlang.{prov,req}.files: recognize compresses BEAMs

* Thu Feb 12 2009 Led <led@altlinux.ru> 0.7.0-alt2
- removed hard requires to erlang

* Wed Jan 14 2009 Led <led@altlinux.ru> 0.7.0-alt1
- 0.7.0
- fixed spec
- removed rpm macros (its in rpm-macros-erlang now)
- rewritten Summary and %%description

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
