%define        gemname progress_bar

Name:          gem-progress-bar
Version:       1.3.3
Release:       alt1
Summary:       Simple Progress Bar for output to a terminal
License:       WTFPL
Group:         Development/Ruby
Url:           http://github.com/paul/progress_bar
Vcs:           https://github.com/paul/progress_bar.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(reek) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(highline) >= 1.6 gem(highline) < 3
BuildRequires: gem(options) >= 2.3.0 gem(options) < 2.4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(highline) >= 1.6 gem(highline) < 3
Requires:      gem(options) >= 2.3.0 gem(options) < 2.4
Provides:      gem(progress_bar) = 1.3.3


%description
Give people feedback about long-running tasks without overloading them with
information: Use a progress bar, like Curl or Wget!


%package       -n gem-progress-bar-doc
Version:       1.3.3
Release:       alt1
Summary:       Simple Progress Bar for output to a terminal documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета progress_bar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(progress_bar) = 1.3.3

%description   -n gem-progress-bar-doc
Simple Progress Bar for output to a terminal documentation files.

Give people feedback about long-running tasks without overloading them with
information: Use a progress bar, like Curl or Wget!

%description   -n gem-progress-bar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета progress_bar.


%package       -n gem-progress-bar-devel
Version:       1.3.3
Release:       alt1
Summary:       Simple Progress Bar for output to a terminal development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета progress_bar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(progress_bar) = 1.3.3
Requires:      gem(rake) >= 0
Requires:      gem(reek) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(timecop) >= 0

%description   -n gem-progress-bar-devel
Simple Progress Bar for output to a terminal development package.

Give people feedback about long-running tasks without overloading them with
information: Use a progress bar, like Curl or Wget!

%description   -n gem-progress-bar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета progress_bar.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.mkd
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-progress-bar-doc
%doc README.mkd
%ruby_gemdocdir

%files         -n gem-progress-bar-devel
%doc README.mkd


%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.3-alt1
- + packaged gem with Ruby Policy 2.0
