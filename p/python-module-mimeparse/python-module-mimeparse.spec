%define module_name mimeparse

Name: python-module-%module_name
Version: 0.1.3
Release: alt1
Group: System/Base
License: BSD License
Summary: A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges
URL: http://pypi.python.org/pypi/mimeparse
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %module_name-%version.tar.gz

BuildRequires: python-module-distribute

%description
This module provides basic functions for handling mime-types. It can handle
matching mime-types against a list of media-ranges. See section 14.1 of 
the HTTP specification [RFC 2616] for a complete explanation.

   http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.1

Contents:
    - parse_mime_type():   Parses a mime-type into its component parts.
    - parse_media_range(): Media-ranges are mime-types with wild-cards and a 'q' quality parameter.
    - quality():           Determines the quality ('q') of a mime-type when compared against a list of media-ranges.
    - quality_parsed():    Just like quality() except the second parameter must be pre-parsed.
    - best_match():        Choose the mime-type with the highest quality ('q') from a list of candidates.

%prep
%setup -n %module_name-%version

%build
%python_build

%install
%python_install
%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc README
%python_sitelibdir/mimeparse*

%changelog
* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.3-alt1
- build for ALT
