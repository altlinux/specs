%define _unpackaged_files_terminate_build 1
%define oname rq

%def_without check

Name: python3-module-%oname
Version: 1.0
Release: alt2

Summary: Simple job queues for Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/rq/
BuildArch: noarch

# Source-url: https://pypi.io/packages/source/r/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-click

%py3_provides %oname


%description
RQ is a simple, lightweight, library for creating background jobs, and
processing them.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if_with check
%check
%__python3 setup.py test
%endif

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Nov 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- python2 disabled

* Wed May 08 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version (1.0) with rpmgs script
- cleanup spec
- temp. disabled check section (obsoleted test uses queue.get_failed_queue)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.2-alt1
- Updated to upstream version 0.9.2.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.6-alt1.git20140917.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt1.git20140917.1
- NMU: Use buildreq for BR.

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20140917
- Initial build for Sisyphus

