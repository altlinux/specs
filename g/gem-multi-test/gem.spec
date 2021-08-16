%define        gemname multi_test

Name:          gem-multi-test
Version:       0.1.2
Release:       alt1
Summary:       multi-test-0.1.2
License:       MIT
Group:         Development/Ruby
Url:           http://cukes.info
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names activesupport,minitest,plain-ruby,rspec,test-unit
Provides:      gem(multi_test) = 0.1.2

%description
Wafter-thin gem to help control rogue test/unit/autorun requires


%package       -n gem-multi-test-doc
Version:       0.1.2
Release:       alt1
Summary:       multi-test-0.1.2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета multi_test
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(multi_test) = 0.1.2

%description   -n gem-multi-test-doc
multi-test-0.1.2 documentation files.

Wafter-thin gem to help control rogue test/unit/autorun requires

%description   -n gem-multi-test-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета multi_test.


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

%files         -n gem-multi-test-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu May 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
