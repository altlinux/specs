%define oname flask-canvas

Name: python3-module-%oname
Version: 0.1
Release: alt2
Summary: A Flask extension for Facebook canvas-based apps
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/flask-canvas/
# https://github.com/demianbrecht/flask-canvas.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
A Flask extension for Facebook canvas-based apps.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc docs/source/*.rst README example
%python3_sitelibdir/*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt2
- disable python2

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt1.git20140214.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20140214.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140214
- Initial build for Sisyphus

