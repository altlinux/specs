%define        gemname awesome_print

Name:          gem-awesome-print
Version:       1.9.2
Release:       alt1
Summary:       Pretty print your Ruby objects with style -- in full color and with proper indentation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/awesome-print/awesome_print
Vcs:           https://github.com/awesome-print/awesome_print.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 3.0.0 gem(rspec) < 4
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(fakefs) >= 0.2.1
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(nokogiri) >= 1.11.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_alias_names awesome_print,awesome-print
Obsoletes:     ruby-awesome-print < %EVR
Provides:      ruby-awesome-print = %EVR
Provides:      gem(awesome_print) = 1.9.2


%description
Awesome Print is a Ruby library that pretty prints Ruby objects in full color
exposing their internal structure with proper indentation. Rails ActiveRecord
objects and usage within Rails templates are supported via included mixins.


%package       -n gem-awesome-print-doc
Version:       1.9.2
Release:       alt1
Summary:       Pretty print your Ruby objects with style -- in full color and with proper indentation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета awesome_print
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(awesome_print) = 1.9.2

%description   -n gem-awesome-print-doc
Pretty print your Ruby objects with style -- in full color and with proper
indentation documentation files.

Awesome Print is a Ruby library that pretty prints Ruby objects in full color
exposing their internal structure with proper indentation. Rails ActiveRecord
objects and usage within Rails templates are supported via included mixins.

%description   -n gem-awesome-print-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета awesome_print.


%package       -n gem-awesome-print-devel
Version:       1.9.2
Release:       alt1
Summary:       Pretty print your Ruby objects with style -- in full color and with proper indentation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета awesome_print
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(awesome_print) = 1.9.2
Requires:      gem(rspec) >= 3.0.0 gem(rspec) < 4
Requires:      gem(appraisal) >= 0
Requires:      gem(fakefs) >= 0.2.1
Requires:      gem(sqlite3) >= 0
Requires:      gem(nokogiri) >= 1.11.0

%description   -n gem-awesome-print-devel
Pretty print your Ruby objects with style -- in full color and with proper
indentation development package.

Awesome Print is a Ruby library that pretty prints Ruby objects in full color
exposing their internal structure with proper indentation. Rails ActiveRecord
objects and usage within Rails templates are supported via included mixins.

%description   -n gem-awesome-print-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета awesome_print.


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

%files         -n gem-awesome-print-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-awesome-print-devel
%doc README.md


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 1.9.2-alt1
- ^ 1.8.0 -> 1.9.2

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus
