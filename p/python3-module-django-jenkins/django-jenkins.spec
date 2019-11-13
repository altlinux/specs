%define oname django-jenkins

Name: python3-module-%oname
Version: 0.19.0
Release: alt2

Summary: Plug and play continuous integration with django and jenkins
License: LGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-jenkins/
# https://github.com/kmmbvnr/django-jenkins.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%add_python3_req_skip flake8.engine


%description
Plug and play continuous integration with Django and Jenkins.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.19.0-alt2
- python2 disabled

* Sun Dec 23 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.19.0-alt1
- update to 0.19.0

* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.16.3-alt2.1
- rebuild with all requires

* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.16.3-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.16.3-alt1.git20140920.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.3-alt1.git20140920
- Initial build for Sisyphus

