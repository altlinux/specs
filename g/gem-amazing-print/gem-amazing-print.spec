%define        gemname amazing_print

Name:          gem-amazing-print
Version:       1.4.0
Release:       alt1
Summary:       Pretty print your Ruby objects with style
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/amazing-print/amazing_print
Vcs:           https://github.com/amazing-print/amazing_print.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(appraisal) >= 2.3 gem(appraisal) < 3
BuildRequires: gem(fakefs) >= 1.2 gem(fakefs) < 2
BuildRequires: gem(nokogiri) >= 1.10 gem(nokogiri) < 2
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-rspec) >= 2.4 gem(rubocop-rspec) < 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names amazing_print,amazing-print
Provides:      gem(amazing_print) = 1.4.0


%description
Pretty print your Ruby objects with style -- in full color and with proper
indentation.

AmazingPrint is a fork of AwesomePrint which became stale and should be used in
its place to avoid conflicts. It is a Ruby library that pretty prints Ruby
objects in full color exposing their internal structure with proper indentation.
Rails ActiveRecord objects and usage within Rails templates are supported via
included mixins.


%package       -n gem-amazing-print-doc
Version:       1.4.0
Release:       alt1
Summary:       Pretty print your Ruby objects with style documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета amazing_print
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(amazing_print) = 1.4.0

%description   -n gem-amazing-print-doc
Pretty print your Ruby objects with style documentation files.

Pretty print your Ruby objects with style -- in full color and with proper
indentation.

AmazingPrint is a fork of AwesomePrint which became stale and should be used in
its place to avoid conflicts. It is a Ruby library that pretty prints Ruby
objects in full color exposing their internal structure with proper indentation.
Rails ActiveRecord objects and usage within Rails templates are supported via
included mixins.

%description   -n gem-amazing-print-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета amazing_print.


%package       -n gem-amazing-print-devel
Version:       1.4.0
Release:       alt1
Summary:       Pretty print your Ruby objects with style development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета amazing_print
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(amazing_print) = 1.4.0
Requires:      gem(appraisal) >= 2.3 gem(appraisal) < 3
Requires:      gem(fakefs) >= 1.2 gem(fakefs) < 2
Requires:      gem(nokogiri) >= 1.10 gem(nokogiri) < 2
Requires:      gem(pry) >= 0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(rubocop) >= 1.15.0 gem(rubocop) < 2
Requires:      gem(rubocop-rspec) >= 2.4.0 gem(rubocop-rspec) < 3

%description   -n gem-amazing-print-devel
Pretty print your Ruby objects with style development package.

Pretty print your Ruby objects with style -- in full color and with proper
indentation.

AmazingPrint is a fork of AwesomePrint which became stale and should be used in
its place to avoid conflicts. It is a Ruby library that pretty prints Ruby
objects in full color exposing their internal structure with proper indentation.
Rails ActiveRecord objects and usage within Rails templates are supported via
included mixins.

%description   -n gem-amazing-print-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета amazing_print.


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

%files         -n gem-amazing-print-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-amazing-print-devel
%doc README.md


%changelog
* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.3.0 -> 1.4.0

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ^ 1.2.2 -> 1.3.0

* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1
- + packaged gem with usage Ruby Policy 2.0
