Name: update-source-functions
Version: 0.1.2
Release: alt1

Summary: A set of functions intended to help with updating a git repository from an upstream source
License: GPLv3
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

Requires: python-module-json

%description
This package contains the set of Shell functions intended to help with
updating a git repository from an upstream source released in a public
directory. Several popular software project hostings are supported
including SourceForge and GitHub. The plain network public directory
(i.e. HTTP, FTP) search is also supported.

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
