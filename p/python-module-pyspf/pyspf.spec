%define version 2.0.13
%define release alt0.1
%def_with python3
%setup_python_module pyspf

Name: %{packagename}
Version: %version
Release: %release
Summary: Python module and programs for SPF (Sender Policy Framework)

Group: Development/Python
License: Python Software Foundation License
Url: https://github.com/sdgathman/pyspf/
Source0: pyspf-%version.tar

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

Requires: python-module-ipaddr python-module-dns

BuildArch: noarch

Packager: L.A. Kostis <lakostis@altlinux.ru>

%description
SPF does email sender validation.  For more information about SPF,
please see http://openspf.org

This SPF client is intended to be installed on the border MTA, checking
if incoming SMTP clients are permitted to send mail.  The SPF check
should be done during the MAIL FROM:<...> command.

%package -n python3-module-%modulename
Summary: Python3 module and programs for SPF (Sender Policy Framework)
Group: Development/Python3
Requires: python3-module-ipaddress python3-module-dns

%description -n python3-module-%modulename
SPF does email sender validation.  For more information about SPF,
please see http://openspf.org

This SPF client is intended to be installed on the border MTA, checking
if incoming SMTP clients are permitted to send mail.  The SPF check
should be done during the MAIL FROM:<...> command.

%prep
%setup -q -n %modulename-%version

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
%python_install --optimize=2 --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install --record=INSTALLED_FILES3
popd
%endif

%files -f INSTALLED_FILES
%exclude %_bindir/*
%doc CHANGELOG PKG-INFO README test

%if_with python3
%files -n python3-module-%modulename -f ../python3/INSTALLED_FILES3
%doc CHANGELOG PKG-INFO README test
%python3_sitelibdir/*
%endif

%changelog
* Sat Sep 28 2019 L.A. Kostis <lakostis@altlinux.ru> 2.0.13-alt0.1
- 2.0.13.
- build python3 module.
- move bin/ to python3 module (due upcoming python deprecation).
- fix requires.

* Mon Aug 31 2015 L.A. Kostis <lakostis@altlinux.ru> 2.0.12-alt0.1
- 2.0.12.

* Wed Jan 07 2015 L.A. Kostis <lakostis@altlinux.ru> 2.0.11-alt0.1
- 2.0.11.

* Fri Aug 03 2012 L.A. Kostis <lakostis@altlinux.ru> 2.0.7-alt0.1
- 2.0.7.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.5-alt0.1.1
- Rebuild with Python-2.7

* Fri Aug 26 2011 L.A. Kostis <lakostis@altlinux.ru> 2.0.5-alt0.1
- Initial build for ALTLinux.

* Wed Apr 02 2008 Stuart Gathman <stuart@bmsi.com> 2.0.5-1
- Add timeout parameter to query ctor and DNSLookup
- Patch from Scott Kitterman to retry truncated results with TCP unless harsh
- Validate DNS labels
- Reflect decision on empty-exp errata
* Wed Jul 25 2007 Stuart Gathman <stuart@bmsi.com> 2.0.4-1
- Correct unofficial 'best guess' processing.
- PTR validation processing cleanup
- Improved detection of exp= errors
- Keyword args for get_header, minor fixes
* Mon Jan 15 2007 Stuart Gathman <stuart@bmsi.com> 2.0.3-1
- pyspf requires pydns, python-pyspf requires python-pydns
- Record matching mechanism and add to Received-SPF header.
- Test for RFC4408 6.2/4, and fix spf.py to comply.
- Test for type SPF (type 99) by default in harsh mode only.
- Permerror for more than one exp or redirect modifier.
- Parse op= modifier
* Sat Dec 30 2006 Stuart Gathman <stuart@bmsi.com> 2.0.2-1
- Update openspf URLs
- Update Readme to better describe available pyspf interfaces
- Add basic description of type99.py and spfquery.py scripts
- Add usage instructions for type99.py DNS RR type conversion script
- Add spfquery.py usage instructions
- Incorporate downstream feedback from Debian packager
- Fix key-value quoting in get_header
* Fri Dec 08 2006 Stuart Gathman <stuart@bmsi.com> 2.0.1-1
- Prevent cache poisoning attack
- Prevent malformed RR attack
- Update license on a few files we missed last time
* Mon Nov 20 2006 Stuart Gathman <stuart@bmsi.com> 2.0-1
- Completed RFC 4408 compliance
- Added spf.check2 for RFC 4408 compatible result codes
- Full IP6 support
- Fedora Core compatible RPM spec file
- Update README, licenses
* Wed Sep 26 2006 Stuart Gathman <stuart@bmsi.com> 1.8-1
- YAML test suite syntax
- trailing dot support (RFC4408 8.1)
* Tue Aug 29 2006 Sean Reifschneider <jafo@tummy.com> 1.7-1
- Initial RPM spec file.
