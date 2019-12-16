Name: update-source-functions
Version: 0.1.10
Release: alt2

Summary: A set of functions intended to help with updating a git repository from an upstream source
License: GPLv3
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

Requires: python3(simplejson)

%description
This package contains the set of Shell functions intended to help with
updating a git repository from an upstream source released in a public
directory. Several popular software project hostings are supported
including SourceForge and GitHub. The plain network public directory
(i.e. HTTP, FTP) search is also supported with a shortcut for PyPI.

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure
%make_build

%install
%makeinstall_std
#%find_lang %name

#%files -f %name.lang
%files
%_bindir/*.sh

%changelog
* Mon Dec 16 2019 Paul Wolneykien <manowar@altlinux.org> 0.1.10-alt2
- Switch to Python 3.

* Thu Jul 10 2014 Paul Wolneykien <manowar@altlinux.org> 0.1.10-alt1
- update_srcdir: Fix: strip 1 path component by default.

* Sat Feb 01 2014 Paul Wolneykien <manowar@altlinux.org> 0.1.9-alt1
- Handle full URIs in a pubdir answer properly.

* Wed Dec 25 2013 Paul Wolneykien <manowar@altlinux.ru> 0.1.8-alt1
- Fix/improve: delete the non-numeric tag prefix by default (GitHub).

* Wed Dec 25 2013 Paul Wolneykien <manowar@altlinux.ru> 0.1.7-alt2
- Use simplejson instead of json for compatibility with older
  Python versions.

* Thu Dec 12 2013 Paul Wolneykien <manowar@altlinux.ru> 0.1.7-alt1
- Use wget which handles SourceForge download URIs properly.
- Make the tarname extraction more smart.

* Wed Dec 11 2013 Paul Wolneykien <manowar@altlinux.ru> 0.1.6-alt1
- Add the set of standard file, spec and Git management functions.

* Fri Oct 25 2013 Paul Wolneykien <manowar@altlinux.ru> 0.1.5-alt1
- Fix directory listing in the pubdir proc.

* Fri May 31 2013 Paul Wolneykien <manowar@altlinux.org> 0.1.4-alt1
- Add proc for a git subtree merge.
- Add support for general git repos.
- Make BASIC_VERPAT allow only numbers in the version string.
- Fix handling of relative URIs.

* Thu Apr 11 2013 Paul Wolneykien <manowar@altlinux.org> 0.1.3-alt1
- Define the basic filename pattern as BASIC_VERPAT.
- Add basic support of the PyPI.
- Add support for HTTP public directories.

* Wed Apr 10 2013 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt1
- Fix version comparison: compare with 0 instead of -1.

* Wed Apr 10 2013 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Fix package requisites: update-source-functions alone should be
  sufficient as the value of "cronbuild_requires" option.
- Update the SourceForge default file pattern: make '.bz2' possible.
- Annotate the output format of the GitHub search function.
- Fix quotation in the rsstail's sed scriptlet.
- Add a public network directory search function.

* Tue Apr 10 2013 Paul Wolneykien <manowar@altlinux.ru> 0.1.0-alt1
- Initial release.
