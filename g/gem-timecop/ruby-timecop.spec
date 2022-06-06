%define        gemname timecop

Name:          gem-timecop
Version:       0.9.5
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

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-timecop < %EVR
Provides:      ruby-timecop = %EVR
Provides:      gem(timecop) = 0.9.5


%description
A gem providing "time travel" and "time freezing" capabilities, making it dead
simple to test time-dependent code. It provides a unified method to mock
Time.now, Date.today, and DateTime.now in a single call.


%package       -n gem-timecop-doc
Version:       0.9.5
Release:       alt1
Summary:       A gem providing "time travel" and "time freezing" capabilities documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета timecop
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(timecop) = 0.9.5

%description   -n gem-timecop-doc
A gem providing "time travel" and "time freezing" capabilities documentation
files.

A gem providing "time travel" and "time freezing" capabilities, making it dead
simple to test time-dependent code. It provides a unified method to mock
Time.now, Date.today, and DateTime.now in a single call.

%description   -n gem-timecop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета timecop.


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


%changelog
* Wed May 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.5-alt1
- ^ 0.9.1 -> 0.9.5

* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 0.9.1-alt1
- Initial build.
