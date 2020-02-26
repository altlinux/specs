%define oname pyspf

Name:       python3-module-%oname
Version:    2.0.14
Release:    alt1

Summary:    Python module and programs for SPF (Sender Policy Framework)
License:    Python-2.0
Group:      Development/Python3
Url:        https://github.com/sdgathman/pyspf/
Packager:   L.A. Kostis <lakostis@altlinux.ru>

BuildArch:  noarch
Requires:   python3-module-dns
BuildPreReq: rpm-build-python3

Source:     pyspf-%version.tar


%description
SPF does email sender validation.  For more information about SPF,
please see http://www.open-spf.org

This SPF client is intended to be installed on the border MTA, checking
if incoming SMTP clients are permitted to send mail.  The SPF check
should be done during the MAIL FROM:<...> command.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install --record=INSTALLED_FILES3

%define _unpackaged_files_terminate_build 1


%files
%doc CHANGELOG PKG-INFO README.md test
%_bindir/*
%python3_sitelibdir/*


%changelog
* Wed Feb 26 2020 Dmitry V. Levin <ldv@altlinux.org> 2.0.14-alt1
- 2.0.13 -> 2.0.14.

* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0.13-alt1
- Build for python2 disabled.

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
