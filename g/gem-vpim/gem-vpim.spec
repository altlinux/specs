%define        pkgname vpim

Name:          gem-%pkgname
Version:       13.11.11
Release:       alt3
Summary:       vPim provides calendaring, scheduling, and contact support for Ruby
License:       GPLv2
Group:         Development/Ruby
Url:           https://github.com/sam-github/vpim
Vcs:           https://github.com/sam-github/vpim.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         13.11.11.1.patch

BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

vPim provides calendaring, scheduling, and contact support for Ruby through
the standard iCalendar and vCard data formats for "personal information"
exchange.


%package       icalendar
Version:       1.1
Summary:       vPim provides calendaring, scheduling, and contact support for Ruby for iCalendar
Group:         Development/Ruby
BuildArch:     noarch

%description   icalendar
%summary.


%package       icalendar-doc
Version:       1.1
Summary:       Documentation files for vpim_icalendar gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vpim_icalendar
Group:         Development/Documentation
BuildArch:     noarch

%description   icalendar-doc
Documentation files for %gemname gem.

%description   icalendar-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       doc
Version:       13.11.11
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup
%patch -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         icalendar
%ruby_gemspecdir/vpim_icalendar-1.1.gemspec
%ruby_gemslibdir/vpim_icalendar-1.1

%files         icalendar-doc
%ruby_gemsdocdir/vpim_icalendar-1.1



%changelog
* Tue May 26 2020 Pavel Skrylev <majioa@altlinux.org> 13.11.11-alt3
- + patch to fix deprectard require to "ubygems"

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 13.11.11-alt2
- > Ruby Policy 2.0
- ! spec tags

* Wed Dec 19 2018 Pavel Skrylev <majioa@altlinux.org> 13.11.11-alt1
- Initial build for Sisyphus bumped to 13.11.11.
