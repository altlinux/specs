%define        gemname reline

Name:          gem-reline
Version:       0.3.1
Release:       alt1
Summary:       Alternative GNU Readline or Editline implementation by pure Ruby
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/ruby/reline
Vcs:           https://github.com/ruby/reline.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(yamatanooroti) >= 0.0.9
BuildRequires: gem(io-console) >= 0.5 gem(io-console) < 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(io-console) >= 0.5 gem(io-console) < 1
Provides:      gem(reline) = 0.3.1


%description
Alternative GNU Readline or Editline implementation by pure Ruby.


%package       -n gem-reline-doc
Version:       0.3.1
Release:       alt1
Summary:       Alternative GNU Readline or Editline implementation by pure Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета reline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(reline) = 0.3.1

%description   -n gem-reline-doc
Alternative GNU Readline or Editline implementation by pure Ruby documentation
files.

%description   -n gem-reline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета reline.


%package       -n gem-reline-devel
Version:       0.3.1
Release:       alt1
Summary:       Alternative GNU Readline or Editline implementation by pure Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета reline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(reline) = 0.3.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(yamatanooroti) >= 0.0.9

%description   -n gem-reline-devel
Alternative GNU Readline or Editline implementation by pure Ruby development
package.

%description   -n gem-reline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета reline.


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

%files         -n gem-reline-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-reline-devel
%doc README.md


%changelog
* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.1-alt1
- + packaged gem with Ruby Policy 2.0
