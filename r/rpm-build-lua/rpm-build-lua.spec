Name: rpm-build-lua
Version: 0.3
Release: alt1

Summary: RPM helpers to build lua packages

License: GPL-3.0-or-later
Group: Development/Other
Url: git://git.altlinux.org/gears/r/rpm-build-lua.git

Source: %name-%version-%release.tar

BuildArch: noarch
Requires: rpm-macros-lua >= 1.5

%description
%summary.

%prep
%setup -n %name-%version-%release

%install
install -p -m0644 -D lua-macros.env %buildroot%_rpmmacrosdir/lua.env
install -p -m0755 -D lua.prov %buildroot%_rpmlibdir/lua.prov
install -p -m0755 -D lua.prov.files %buildroot%_rpmlibdir/lua.prov.files
install -p -m0755 -D lua.req %buildroot%_rpmlibdir/lua.req
install -p -m0755 -D lua.req.files %buildroot%_rpmlibdir/lua.req.files

%files
%_rpmmacrosdir/lua.*
%_rpmlibdir/lua.*

%changelog
* Wed Mar 22 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.3-alt1
- lua.req.files: skip ELF files (thanks Egor Ignatov <egori@altlinux.org>)

* Sun Mar 19 2023 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.2-alt1
- Fixed autoreq.

* Wed Jun 29 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1-alt1
- Initial build for ALT Sisyphus.
