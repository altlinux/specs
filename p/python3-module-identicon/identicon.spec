%define _unpackaged_files_terminate_build 1
%define oname identicon

Name: python3-module-%oname
Version: 20101207
Release: alt3

Summary: Python identicon implementation
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://github.com/aerosol/identicon
# https://github.com/aerosol/identicon.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires PIL


%description
identicon.py: identicon python implementation.

%prep
%setup

## py2 -> py3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 20101207-alt3
- python2 disabled

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 20101207-alt2.qa1
- NMU: applied repocop patch

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 20101207-alt2
- NMU: rebuilt to regenerate dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 20101207-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 20101207-alt1.1
- NMU: Use buildreq for BR.

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20101207-alt1
- Initial build for Sisyphus

