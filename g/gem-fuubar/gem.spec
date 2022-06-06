%define        gemname fuubar

Name:          gem-fuubar
Version:       2.5.1
Release:       alt1
Summary:       the instafailing RSpec progress bar formatter
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/thekompanee/fuubar
Vcs:           https://github.com/thekompanee/fuubar.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec-core) >= 3.0 gem(rspec-core) < 4
BuildRequires: gem(ruby-progressbar) >= 1.4 gem(ruby-progressbar) < 2
BuildRequires: gem(rspec) >= 3.7 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec-core) >= 3.0 gem(rspec-core) < 4
Requires:      gem(ruby-progressbar) >= 1.4 gem(ruby-progressbar) < 2
Provides:      gem(fuubar) = 2.5.1


%description
fuubar is an instafailing RSpec formatter that uses a progress bar instead of a
string of letters and dots as feedback.


%package       -n gem-fuubar-doc
Version:       2.5.1
Release:       alt1
Summary:       the instafailing RSpec progress bar formatter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fuubar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fuubar) = 2.5.1

%description   -n gem-fuubar-doc
the instafailing RSpec progress bar formatter documentation files.

fuubar is an instafailing RSpec formatter that uses a progress bar instead of a
string of letters and dots as feedback.

%description   -n gem-fuubar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fuubar.


%package       -n gem-fuubar-devel
Version:       2.5.1
Release:       alt1
Summary:       the instafailing RSpec progress bar formatter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fuubar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fuubar) = 2.5.1
Requires:      gem(rspec) >= 3.7 gem(rspec) < 4

%description   -n gem-fuubar-devel
the instafailing RSpec progress bar formatter development package.

fuubar is an instafailing RSpec formatter that uses a progress bar instead of a
string of letters and dots as feedback.

%description   -n gem-fuubar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fuubar.


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

%files         -n gem-fuubar-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fuubar-devel
%doc README.md


%changelog
* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt1
- + packaged gem with Ruby Policy 2.0
