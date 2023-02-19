%define        gemname record_tag_helper

Name:          gem-record-tag-helper
Version:       1.0.1.1
Release:       alt0.1
Summary:       ActionView Record Tag Helpers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/record_tag_helper
Vcs:           https://github.com/rails/record_tag_helper.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(actionpack) >= 5
BuildRequires: gem(activemodel) >= 5
BuildRequires: gem(rake) >= 0
BuildRequires: gem(mocha) >= 1.1.0
BuildRequires: gem(actionview) >= 5
BuildRequires: gem(rubocop) >= 0.68.0
BuildConflicts: gem(mocha) >= 2
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names record_tag_helper,record-tag-helper
Requires:      gem(actionview) >= 5
Obsoletes:     ruby-record_tag_helper < %EVR
Provides:      ruby-record_tag_helper = %EVR
Provides:      gem(record_tag_helper) = 1.0.1.1

%ruby_use_gem_version record_tag_helper:1.0.1.1

%description
RecordTagHelper consists of code that was formerly a part of ActionView, but has
been removed from core in Rails 5. This gem is provided to ensure projects that
use functionality from ActionView::Helpers::RecordTagHelper have an appropriate
upgrade path.

This gem provides methods for generating container tags, such as div, for your
record. This is the recommended way of creating a container for your Active
Record object, as it adds appropriate class and id attributes to that container.
You can then refer to those containers easily by following that convention,
instead of having to think about which class or id attribute you should use.


%package       -n gem-record-tag-helper-doc
Version:       1.0.1.1
Release:       alt0.1
Summary:       ActionView Record Tag Helpers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета record_tag_helper
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(record_tag_helper) = 1.0.1.1

%description   -n gem-record-tag-helper-doc
ActionView Record Tag Helpers documentation files.

RecordTagHelper consists of code that was formerly a part of ActionView, but has
been removed from core in Rails 5. This gem is provided to ensure projects that
use functionality from ActionView::Helpers::RecordTagHelper have an appropriate
upgrade path.

This gem provides methods for generating container tags, such as div, for your
record. This is the recommended way of creating a container for your Active
Record object, as it adds appropriate class and id attributes to that container.
You can then refer to those containers easily by following that convention,
instead of having to think about which class or id attribute you should use.

%description   -n gem-record-tag-helper-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета record_tag_helper.


%package       -n gem-record-tag-helper-devel
Version:       1.0.1.1
Release:       alt0.1
Summary:       ActionView Record Tag Helpers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета record_tag_helper
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(record_tag_helper) = 1.0.1.1
Requires:      gem(i18n) >= 0
Requires:      gem(nokogiri) >= 0
Requires:      gem(actionpack) >= 5
Requires:      gem(activemodel) >= 5
Requires:      gem(rake) >= 0
Requires:      gem(mocha) >= 1.1.0
Requires:      gem(rubocop) >= 0.68.0
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(rubocop) >= 2

%description   -n gem-record-tag-helper-devel
ActionView Record Tag Helpers development package.

RecordTagHelper consists of code that was formerly a part of ActionView, but has
been removed from core in Rails 5. This gem is provided to ensure projects that
use functionality from ActionView::Helpers::RecordTagHelper have an appropriate
upgrade path.

This gem provides methods for generating container tags, such as div, for your
record. This is the recommended way of creating a container for your Active
Record object, as it adds appropriate class and id attributes to that container.
You can then refer to those containers easily by following that convention,
instead of having to think about which class or id attribute you should use.

%description   -n gem-record-tag-helper-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета record_tag_helper.


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

%files         -n gem-record-tag-helper-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-record-tag-helper-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.1.1-alt0.1
- ^ 1.0.1 -> 1.0.1[1]

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- > Ruby Policy 2.0
- ^ 1.0.0 -> 1.0.1
- ! spec tags

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial gemified build for Sisyphus
