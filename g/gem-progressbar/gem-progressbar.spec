%define        _unpackaged_files_terminate_build 1
%define        gemname progressbar

Name:          gem-progressbar
Version:       1.13.0
Release:       alt1
Summary:       Ruby/ProgressBar is a text progress bar library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jfelchner/ruby-progressbar
Vcs:           https://github.com/jfelchner/ruby-progressbar.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(awesome_print) >= 1.6
BuildRequires: gem(ruby-prof) >= 1.6
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(rspectacular) >= 0.70.6
BuildRequires: gem(fuubar) >= 2.3
BuildRequires: gem(timecop) >= 0.9
BuildConflicts: gem(awesome_print) >= 2
BuildConflicts: gem(ruby-prof) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspectacular) >= 0.71
BuildConflicts: gem(fuubar) >= 3
BuildConflicts: gem(timecop) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-progressbar < %EVR
Provides:      ruby-progressbar = %EVR
Provides:      gem(progressbar) = 1.13.0

%description
The ultimate text progress bar library for Ruby! It'll SMASH YOU OVER THE HEAD
with a PURE RUSH of progress bar excitement!

Don't miss out on what all the kids are talking about! If you want everyone to
know that your gem or app can survive in the cage then YOU WANT
RUBY-PROGRESSBAR!


%package       -n gem-ruby-progressbar
Version:       1.13.0
Release:       alt1
Summary:       Ruby/ProgressBar is a text progress bar library for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(ruby-progressbar) = 1.13.0

%description   -n gem-ruby-progressbar
Ruby/ProgressBar is a text progress bar library for Ruby.


%package       -n gem-ruby-progressbar-doc
Version:       1.13.0
Release:       alt1
Summary:       Ruby/ProgressBar is a text progress bar library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-progressbar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-progressbar) = 1.13.0

%description   -n gem-ruby-progressbar-doc
Ruby/ProgressBar is a text progress bar library for Ruby documentation files.

%description   -n gem-ruby-progressbar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-progressbar.


%package       -n gem-ruby-progressbar-devel
Version:       1.13.0
Release:       alt1
Summary:       Ruby/ProgressBar is a text progress bar library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-progressbar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-progressbar) = 1.13.0

%description   -n gem-ruby-progressbar-devel
Ruby/ProgressBar is a text progress bar library for Ruby development package.

%description   -n gem-ruby-progressbar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-progressbar.


%package       -n gem-progressbar-doc
Version:       1.13.0
Release:       alt1
Summary:       Ruby/ProgressBar is a text progress bar library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета progressbar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(progressbar) = 1.13.0

%description   -n gem-progressbar-doc
Ruby/ProgressBar is a text progress bar library for Ruby documentation files.

%description   -n gem-progressbar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета progressbar.



%package       -n gem-progressbar-devel
Version:       1.13.0
Release:       alt1
Summary:       Ruby/ProgressBar is a text progress bar library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета progressbar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(progressbar) = 1.13.0

%description   -n gem-progressbar-devel
Ruby/ProgressBar is a text progress bar library for Ruby development package.

%description   -n gem-progressbar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета progressbar.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-ruby-progressbar
%ruby_gemspecdir/ruby-progressbar-1.13.0.gemspec
%ruby_gemslibdir/ruby-progressbar-1.13.0

%files         -n gem-ruby-progressbar-doc
%ruby_gemsdocdir/ruby-progressbar-1.13.0

%files         -n gem-ruby-progressbar-devel

%files         -n gem-progressbar-doc
%ruby_gemdocdir

%files         -n gem-progressbar-devel


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- ^ 1.10.1 -> 1.13.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt1
- updated (^) 1.10.0 -> 1.10.1
- fixed (!) spec

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.0-alt2
- used (>) Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus
