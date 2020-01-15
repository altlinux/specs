%define oname libnacl

Name: python3-module-%oname
Version: 1.7.1
Release: alt1

Summary: This library is used to gain direct access to the functions exposed by Daniel J. Bernstein's nacl library via libsodium or tweetnacl

License: ASL 2.0
Group: Development/Python
Url: https://github.com/saltstack/libnacl
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setupdocs

Requires: libsodium23


%description
This library is used to gain direct access to the functions exposed by
Daniel J. Bernstein's nacl library via libsodium or tweetnacl. It has
been constructed to maintain extensive documentation on how to use nacl
as well as being completely portable. The file in libnacl/__init__.py
can be pulled out and placed directly in any project to give a single
file binding to all of nacl.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS LICENSE MANIFEST.in README.rst
%python3_sitelibdir/*


%changelog
* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.7.1-alt1
- Version updated to 1.7.1
- porting on python3

* Mon Feb 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2.1
- NMU: autorebuild with libsodium-1.0.16 (libsodium23)

* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 1.5.0-alt2
- rebuild with libsodium18

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.0-alt1
- New version

* Fri Jun 24 2016 Lenar Shakirov <snejok@altlinux.ru> 1.4.5-alt2
- Requires: libsodium13 added

* Fri Jun 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.5-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.2-alt1
- New version

* Thu Feb 12 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.0-alt1
- Initial build for ALT

