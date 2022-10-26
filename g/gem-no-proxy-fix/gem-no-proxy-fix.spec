%define        gemname no_proxy_fix

Name:          gem-no-proxy-fix
Version:       0.1.2
Release:       alt1
Summary:       A fix for a no_proxy bug on ruby 2.4.0 and 2.4.1
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ermaker/no_proxy_fix
Vcs:           https://github.com/ermaker/no_proxy_fix.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rspec-its) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(guard) >= 0
BuildRequires: gem(guard-bundler) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(guard-rubocop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(no_proxy_fix) = 0.1.2


%description
A fix for a no_proxy bug:
https://github.com/ruby/ruby/commit/556e3da4216c926e71dea9ce4ea4a08dcfdc1275


%package       -n gem-no-proxy-fix-doc
Version:       0.1.2
Release:       alt1
Summary:       A fix for a no_proxy bug on ruby 2.4.0 and 2.4.1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета no_proxy_fix
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(no_proxy_fix) = 0.1.2

%description   -n gem-no-proxy-fix-doc
A fix for a no_proxy bug on ruby 2.4.0 and 2.4.1 documentation files.

A fix for a no_proxy bug:
https://github.com/ruby/ruby/commit/556e3da4216c926e71dea9ce4ea4a08dcfdc1275

%description   -n gem-no-proxy-fix-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета no_proxy_fix.


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

%files         -n gem-no-proxy-fix-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
