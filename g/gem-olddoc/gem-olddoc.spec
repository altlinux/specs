%define        pkgname olddoc

Name:          gem-%pkgname
Version:       1.8.0
Release:       alt1
Summary:       old-fashioned Ruby documentation generator
Group:         Development/Ruby
License:       MIT
URL:           https://80x24.org/olddoc/
Vcs:           https://80x24.org/olddoc.git
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


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n %pkgname
Summary:       old-fashioned Ruby documentation generator CLI
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable CLI for old-fashioned Ruby documentation generator

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/*

%changelog
* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- > Ruby Policy 2.0
- ^ 1.6.0 -> 1.8.0

* Mon Feb 04 2019 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- Initial build for ALT.
