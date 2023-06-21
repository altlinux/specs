%define        _unpackaged_files_terminate_build 1
%define        gemname timecop

Name:          gem-timecop
Version:       0.9.6
Release:       alt1
Summary:       A gem providing "time travel" and "time freezing" capabilities
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/travisjeffery/timecop
Vcs:           https://github.com/travisjeffery/timecop.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(tzinfo) >= 0
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-rg) >= 0
BuildConflicts: gem(jeweler) >= 2.1.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-timecop < %EVR
Provides:      ruby-timecop = %EVR
Provides:      gem(timecop) = 0.9.6


%description
A gem providing "time travel" and "time freezing" capabilities, making it dead
simple to test time-dependent code. It provides a unified method to mock
Time.now, Date.today, and DateTime.now in a single call.


%package       -n gem-timecop-doc
Version:       0.9.6
Release:       alt1
Summary:       A gem providing "time travel" and "time freezing" capabilities documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета timecop
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(timecop) = 0.9.6

%description   -n gem-timecop-doc
A gem providing "time travel" and "time freezing" capabilities documentation
files.

A gem providing "time travel" and "time freezing" capabilities, making it dead
simple to test time-dependent code. It provides a unified method to mock
Time.now, Date.today, and DateTime.now in a single call.

%description   -n gem-timecop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета timecop.


%package       -n gem-timecop-devel
Version:       0.9.6
Release:       alt1
Summary:       A gem providing "time travel" and "time freezing" capabilities development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета timecop
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(timecop) = 0.9.6
Requires:      gem(rake) >= 0
Requires:      gem(nokogiri) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(activesupport) >= 0
Requires:      gem(tzinfo) >= 0
Requires:      gem(i18n) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-rg) >= 0
Conflicts:     gem(jeweler) >= 2.1.3

%description   -n gem-timecop-devel
A gem providing "time travel" and "time freezing" capabilities development
package.

A gem providing "time travel" and "time freezing" capabilities, making it dead
simple to test time-dependent code. It provides a unified method to mock
Time.now, Date.today, and DateTime.now in a single call.

%description   -n gem-timecop-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета timecop.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-timecop-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-timecop-devel
%doc README.markdown


%changelog
* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.6-alt1
- ^ 0.9.5 -> 0.9.6

* Wed May 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.5-alt1
- ^ 0.9.1 -> 0.9.5

* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 0.9.1-alt1
- Initial build.
