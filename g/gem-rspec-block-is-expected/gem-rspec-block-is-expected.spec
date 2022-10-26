%define        gemname rspec-block_is_expected

Name:          gem-rspec-block-is-expected
Version:       1.0.2
Release:       alt1
Summary:       Simplify testing of blocks in RSpec via block_is_expected
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pboling/rspec-block_is_expected
Vcs:           https://github.com/pboling/rspec-block_is_expected.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec-core) >= 0
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(bundler) >= 1.16 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 3.8 gem(rspec) < 4
BuildRequires: gem(rspec-pending_for) >= 0.1 gem(rspec-pending_for) < 1
BuildRequires: gem(wwtd) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(rspec-core) >= 0
Provides:      gem(rspec-block_is_expected) = 1.0.2


%description
subject { Integer(nil) }; it('raises') { block_is_expected.to
raise_error(TypeError) }


%package       -n gem-rspec-block-is-expected-doc
Version:       1.0.2
Release:       alt1
Summary:       Simplify testing of blocks in RSpec via block_is_expected documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-block_is_expected
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-block_is_expected) = 1.0.2

%description   -n gem-rspec-block-is-expected-doc
Simplify testing of blocks in RSpec via block_is_expected documentation
files.

subject { Integer(nil) }; it('raises') { block_is_expected.to
raise_error(TypeError) }

%description   -n gem-rspec-block-is-expected-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-block_is_expected.


%package       -n gem-rspec-block-is-expected-devel
Version:       1.0.2
Release:       alt1
Summary:       Simplify testing of blocks in RSpec via block_is_expected development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-block_is_expected
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-block_is_expected) = 1.0.2
Requires:      gem(appraisal) >= 0
Requires:      gem(bundler) >= 1.16 gem(bundler) < 3
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3.8 gem(rspec) < 4
Requires:      gem(rspec-pending_for) >= 0.1 gem(rspec-pending_for) < 1
Requires:      gem(wwtd) >= 0

%description   -n gem-rspec-block-is-expected-devel
Simplify testing of blocks in RSpec via block_is_expected development
package.

subject { Integer(nil) }; it('raises') { block_is_expected.to
raise_error(TypeError) }

%description   -n gem-rspec-block-is-expected-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-block_is_expected.


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

%files         -n gem-rspec-block-is-expected-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-block-is-expected-devel
%doc README.md


%changelog
* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
