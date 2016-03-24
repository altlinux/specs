%define inversion 2
%define pyversion 3.6
%define reldate 20160323

Name: python-sphinx-objects.inv
Version: %inversion.%pyversion.%reldate
Release: alt1
Summary: Sphinx inventory version %inversion
License: BSD
Group: Development/Python
Packager: Python Development Team <python@packages.altlinux.org>
Url: https://docs.python.org/dev/objects.inv
Source: %url
BuildArch: noarch

%description
This package contains periodically updated Sphinx inventory version %inversion
for Python %pyversion.

%install
mkdir -p %buildroot%_datadir/python-sphinx
install -pDm644 %SOURCE0 %buildroot%_datadir/python-sphinx/objects.inv

%files
%_datadir/python-sphinx/

%changelog
* Thu Mar 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160323-alt1
- repocop cronbuild 20160324. At your service.

* Tue Mar 22 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160322-alt1
- repocop cronbuild 20160322. At your service.

* Mon Mar 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160321-alt1
- repocop cronbuild 20160321. At your service.

* Sun Mar 20 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160319-alt1
- repocop cronbuild 20160320. At your service.

* Sat Mar 19 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160318-alt1
- repocop cronbuild 20160319. At your service.

* Mon Mar 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160314-alt1
- repocop cronbuild 20160314. At your service.

* Sat Mar 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160311-alt1
- repocop cronbuild 20160312. At your service.

* Tue Mar 08 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160307-alt1
- repocop cronbuild 20160308. At your service.

* Fri Feb 26 2016 Dmitry V. Levin <ldv@altlinux.org> 2.3.6.20160226-alt1
- Initial revision.
