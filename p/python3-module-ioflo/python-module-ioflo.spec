%define oname ioflo

Name: python3-module-%oname
Version: 2.0.0
Release: alt2

Summary: Flow Based Programming Automated Reasoning Engine and Automation Operation System

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/ioflo/ioflo.git
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar
Patch0: port-on-python3.patch

# For more detailed autoreqs (to be on the safer side).
%python3_req_hier

BuildRequires(pre): rpm-build-python3

%description
IoFlo is configured in a convenient user friendly scripting language
called FloScript.

%prep
%setup
%patch0 -p1

%build
%add_optflags -fno-strict-aliasing
%python3_build


%install
%python3_install

%files
%doc ChangeLog.md LEGAL LICENSE LICENSE-2.0.txt README.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- Fixed BuildRequires.
- Fixed License tag.

* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt1
- Version updated to 2.0.0
- porting on python3

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.6.5-alt1
- New version

* Thu Jun 16 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.5-alt2
- %%python_req_hier -- for more detailed autoreqs (to be on the safer side).

* Fri Jun 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.5-alt1
- New version

* Mon Aug 31 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.2.1-alt3
- Add cleanup for tests-dir, another try

* Fri May 29 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.2.1-alt2
- Add cleanup for tests-dir

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.2.1-alt1
- New version

* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.0.2-alt1
- Initial build for ALT

