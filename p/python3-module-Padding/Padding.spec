%define oname Padding

Name: python3-module-%oname
Version: 0.5
Release: alt1

Summary: Padding methods for password based encryption
License: Public domain
Group: Development/Python3
Url: https://pypi.python.org/pypi/Padding/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
Padding methods for password based encryption.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
python3 -c "from Padding import *"

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5-alt1
- version updated to 0.5
- disable python2, enable python3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.1
- NMU: Use buildreq for BR.

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

