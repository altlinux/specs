%define        gemname appraisal

Name:          gem-appraisal
Version:       2.4.1
Release:       alt1
Summary:       Find out what your Ruby gems are worth
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/thoughtbot/appraisal
Vcs:           https://github.com/thoughtbot/appraisal.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(thor) >= 0.14.0
BuildRequires: gem(activesupport) >= 3.2.21
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(thor) >= 0.14.0
Provides:      gem(appraisal) = 2.4.1


%description
Appraisal integrates with bundler and rake to test your library against
different versions of dependencies in repeatable scenarios called "appraisals."


%package       -n appraisal
Version:       2.4.1
Release:       alt1
Summary:       Find out what your Ruby gems are worth executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета appraisal
Group:         Other
BuildArch:     noarch

Requires:      gem(appraisal) = 2.4.1

%description   -n appraisal
Find out what your Ruby gems are worth executable(s).

Appraisal integrates with bundler and rake to test your library against
different versions of dependencies in repeatable scenarios called "appraisals."

%description   -n appraisal -l ru_RU.UTF-8
Исполнямка для самоцвета appraisal.


%package       -n gem-appraisal-doc
Version:       2.4.1
Release:       alt1
Summary:       Find out what your Ruby gems are worth documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета appraisal
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(appraisal) = 2.4.1

%description   -n gem-appraisal-doc
Find out what your Ruby gems are worth documentation files.

Appraisal integrates with bundler and rake to test your library against
different versions of dependencies in repeatable scenarios called "appraisals."

%description   -n gem-appraisal-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета appraisal.


%package       -n gem-appraisal-devel
Version:       2.4.1
Release:       alt1
Summary:       Find out what your Ruby gems are worth development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета appraisal
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(appraisal) = 2.4.1
Requires:      gem(activesupport) >= 3.2.21
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-appraisal-devel
Find out what your Ruby gems are worth development package.

Appraisal integrates with bundler and rake to test your library against
different versions of dependencies in repeatable scenarios called "appraisals."

%description   -n gem-appraisal-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета appraisal.


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

%files         -n appraisal
%doc README.md
%_bindir/appraisal

%files         -n gem-appraisal-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-appraisal-devel
%doc README.md


%changelog
* Mon Oct 10 2022 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt1
- ^ 2.4.0 -> 2.4.1

* Mon Jun 21 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- + packaged gem with Ruby Policy 2.0
