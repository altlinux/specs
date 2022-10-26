%define        gemname rspec-pending_for

Name:          gem-rspec-pending-for
Version:       0.1.16
Release:       alt1
Summary:       Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) / version combinations
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pboling/rspec-pending_for
Vcs:           https://github.com/pboling/rspec-pending_for.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec-core) >= 0
BuildRequires: gem(ruby_engine) >= 1 gem(ruby_engine) < 3
BuildRequires: gem(ruby_version) >= 1.0 gem(ruby_version) < 2
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(minitest) >= 5.3 gem(minitest) < 6
BuildRequires: gem(rspec) >= 3 gem(rspec) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec-core) >= 0
Requires:      gem(ruby_engine) >= 1 gem(ruby_engine) < 3
Requires:      gem(ruby_version) >= 1.0 gem(ruby_version) < 2
Provides:      gem(rspec-pending_for) = 0.1.16

%description
Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) /
version combinations.


%package       -n gem-rspec-pending-for-doc
Version:       0.1.16
Release:       alt1
Summary:       Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) / version combinations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-pending_for
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-pending_for) = 0.1.16

%description   -n gem-rspec-pending-for-doc
Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) /
version combinations documentation files.

%description   -n gem-rspec-pending-for-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-pending_for.


%package       -n gem-rspec-pending-for-devel
Version:       0.1.16
Release:       alt1
Summary:       Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) / version combinations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-pending_for
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-pending_for) = 0.1.16
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 5.3 gem(minitest) < 6
Requires:      gem(rspec) >= 3 gem(rspec) < 4

%description   -n gem-rspec-pending-for-devel
Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) /
version combinations development package.

%description   -n gem-rspec-pending-for-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-pending_for.


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

%files         -n gem-rspec-pending-for-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-pending-for-devel
%doc README.md


%changelog
* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.16-alt1
- + packaged gem with Ruby Policy 2.0
