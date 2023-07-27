%define  modulename injector

Name:    python3-module-%modulename
Version: 0.21.0
Release: alt1

Summary: Python dependency injection framework, inspired by Guice
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/alecthomas/injector

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
While dependency injection is easy to do in Python due to its support for
keyword arguments, the ease with which objects can be mocked and its dynamic
nature, a framework for assisting in this process can remove a lot of
boiler-plate from larger applications. That's where Injector can help. It
automatically and transitively provides dependencies for you. As an added
benefit, Injector encourages nicely compartmentalised code through the use of
:ref:modules <module>.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Jul 27 2023 Andrey Cherepanov <cas@altlinux.org> 0.21.0-alt1
- New version.

* Wed Aug 17 2022 Andrey Cherepanov <cas@altlinux.org> 0.20.1-alt1
- New version.

* Wed Jun 15 2022 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version.

* Mon Jun 06 2022 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1
- Initial build for Sisyphus.
