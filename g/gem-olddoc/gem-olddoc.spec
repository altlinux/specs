%define        pkgname olddoc

Name:          gem-%pkgname
Version:       1.6.0
Release:       alt1
Summary:       old-fashioned Ruby documentation generator
Group:         Development/Ruby
License:       MIT
URL:           https://80x24.org/olddoc/
# VCS:         https://80x24.org/olddoc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       %pkgname.gemspec
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc)

%description
olddoc contains old-fashioned document generators for those who do not
wish to impose bloated, new-fangled web cruft on their readers.

olddoc contains oldweb, an HTML generator without any images, frames,
CSS, or JavaScript.  It is designed for users of text-based browsers
and/or low-bandwidth connections.  oldweb focuses on text as it is
the lowest common denominator for accessibility and compatibility
with people and hardware.


%package       -n %pkgname
Summary:       old-fashioned Ruby documentation generator CLI
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %pkgname
Executable CLI for old-fashioned Ruby documentation generator

%package       doc
Summary:       Documentation for %pkgname
Group:         Development/Documentation
BuildArch:     noarch

%description doc
%summary.

%prep
%setup
%update_setup_rb
cp %SOURCE1 %pkgname.gemspec

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/

%files -n %pkgname
%_bindir/*

%changelog
* Mon Feb 04 2019 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- Initial build for ALT.
