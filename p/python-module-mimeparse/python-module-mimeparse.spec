%define _unpackaged_files_terminate_build 1

%define oname mimeparse

%def_with python3

Name: python-module-%oname
Version: 1.6.0
Release: alt1%ubt
Summary: Basic functions for handling mime-types in python
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/python-mimeparse

# https://github.com/dbtsai/python-mimeparse.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-dev python-module-setuptools
BuildRequires: python2.7(json)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(json)
%endif

%description
This module provides basic functions for handling mime-types. It can handle
matching mime-types against a list of media-ranges. See section 14.1 of 
the HTTP specification [RFC 2616] for a complete explanation.

   http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.1

Contents:
    - parse_mime_type():   Parses a mime-type into its component parts.
    - parse_media_range(): Media-ranges are mime-types with wild-cards
      and a 'q' quality parameter.
    - quality():           Determines the quality ('q') of a mime-type
      when compared against a list of media-ranges.
    - quality_parsed():    Just like quality() except the second
      parameter must be pre-parsed.
    - best_match():        Choose the mime-type with the highest quality
      ('q') from a list of candidates.

%if_with python3
%package -n python3-module-%oname
Summary: Basic functions for handling mime-types in python
Group: Development/Python3

%description -n python3-module-%oname
This module provides basic functions for handling mime-types. It can handle
matching mime-types against a list of media-ranges. See section 14.1 of 
the HTTP specification [RFC 2616] for a complete explanation.

   http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.1

Contents:
    - parse_mime_type():   Parses a mime-type into its component parts.
    - parse_media_range(): Media-ranges are mime-types with wild-cards
      and a 'q' quality parameter.
    - quality():           Determines the quality ('q') of a mime-type
      when compared against a list of media-ranges.
    - quality_parsed():    Just like quality() except the second
      parameter must be pre-parsed.
    - best_match():        Choose the mime-type with the highest quality
      ('q') from a list of candidates.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python mimeparse_test.py

%if_with python3
pushd ../python3
python3 mimeparse_test.py
popd
%endif


%files
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.0-alt1%ubt
- Updated to upstream version 1.6.0.

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.svn20130102.1.1.1.1
- (AUTO) subst_x86_64.

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.svn20130102.1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.svn20130102.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.svn20130102.1
- NMU: Use buildreq for BR.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.svn20130102
- Version 0.1.4
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.3-alt1
- build for ALT
