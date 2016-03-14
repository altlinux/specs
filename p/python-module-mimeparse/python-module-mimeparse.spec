%define module_name mimeparse

%def_with python3

Name: python-module-%module_name
Version: 0.1.4
Release: alt1.svn20130102.1.1
Group: Development/Python
License: BSD License
Summary: A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges
URL: http://pypi.python.org/pypi/mimeparse
# http://mimeparse.googlecode.com/svn/trunk/
Source: %module_name-%version.tar.gz

#BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

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

%package -n python3-module-%module_name
Summary: A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges
Group: Development/Python3

%description -n python3-module-%module_name
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

%prep
%setup -n %module_name-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc README
%python_sitelibdir/mimeparse*

%if_with python3
%files -n python3-module-%module_name
%doc README
%python3_sitelibdir/mimeparse*
%python3_sitelibdir/__pycache__/*
%endif

%changelog
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
