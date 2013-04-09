Name: update-source-functions
Version: 0.1.0
Release: alt1

Summary: A set of functions intended to help with updating a git repository from an upstream source
License: GPLv3
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

%description
This package contains the set of Shell functions intended to help with
updating a git repository from an upstream source released in a public
directory. Several popular software project hostings are supported
including SourceForge and GitHub.

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
* Tue Apr 10 2013 Paul Wolneykien <manowar@altlinux.ru> 0.1.0-alt1
- Initial release.
