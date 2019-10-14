%define  modulename sphinxcontrib-programoutput

Name:    python3-module-%modulename
Version: 0.15
Release: alt1

Summary: Sphinx extension for capturing program output

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://github.com/NextThought/sphinxcontrib-programoutput

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
A Sphinx extension to literally insert the output of arbitrary commands into
documents, helping you to keep your command examples up to date.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/sphinxcontrib/programoutput
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Mon Oct 14 2019 Grigory Ustinov <grenka@altlinux.org> 0.15-alt1
- Build new version.

* Thu Aug 15 2019 Grigory Ustinov <grenka@altlinux.org> 0.14-alt1
- Build new version.
- Build for python3.
- Transfer to specsubst scheme.

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.8-alt1.1
- (NMU) rebuild with python3.6

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus
