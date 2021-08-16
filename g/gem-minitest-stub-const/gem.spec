%define        gemname minitest-stub-const

Name:          gem-minitest-stub-const
Version:       0.6
Release:       alt1
Summary:       Stub constants for the duration of a block in MiniTest
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/adammck/minitest-stub-const
Vcs:           https://github.com/adammck/minitest-stub-const.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(minitest-stub-const) = 0.6

%description
Stub constants for the duration of a block in MiniTest.
Similar to RSpec's [stub_const] rspec.


%package       -n gem-minitest-stub-const-doc
Version:       0.6
Release:       alt1
Summary:       Stub constants for the duration of a block in MiniTest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-stub-const
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-stub-const) = 0.6

%description   -n gem-minitest-stub-const-doc
Stub constants for the duration of a block in MiniTest documentation files.

Stub constants for the duration of a block in MiniTest.
Similar to RSpec's [stub_const] rspec.

%description   -n gem-minitest-stub-const-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-stub-const.


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

%files         -n gem-minitest-stub-const-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 0.6-alt1
- + packaged gem with Ruby Policy 2.0
