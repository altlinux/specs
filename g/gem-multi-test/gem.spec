%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname multi_test

Name:          gem-multi-test
Version:       1.1.0
Release:       alt1
Summary:       multi-test-1.1.0
License:       MIT
Group:         Development/Ruby
Url:           http://cukes.info
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names multi_test,multi-test
%ruby_ignore_names activesupport,minitest,plain-ruby,rspec,test-unit
Requires:      ruby >= 2.0
Requires:      rubygems >= 1.6.1
Provides:      gem(multi_test) = 1.1.0

%description
Wafter-thin gem to help control rogue test/unit/autorun requires


%if_enabled    doc
%package       -n gem-multi-test-doc
Version:       1.1.0
Release:       alt1
Summary:       multi-test-1.1.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета multi_test
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(multi_test) = 1.1.0

%description   -n gem-multi-test-doc
multi-test-1.1.0 documentation files.

Wafter-thin gem to help control rogue test/unit/autorun requires

%description   -n gem-multi-test-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета multi_test.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-multi-test-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif


%changelog
* Mon Jul 06 2026 Alexander Burmatov <thatman@altlinux.org> 1.1.0-alt1
- ^ 0.1.2 -> 1.1.0

* Thu May 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
