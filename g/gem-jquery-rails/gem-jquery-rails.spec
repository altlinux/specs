%define        gemname jquery-rails

Name:          gem-jquery-rails
Version:       4.5.0
Release:       alt1
Summary:       Use jQuery with Rails 4+
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/jquery-rails
Vcs:           https://github.com/rails/jquery-rails.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rails) >= 0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(json) >= 2
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(railties) >= 4.2.0
BuildRequires: gem(thor) >= 0.14
BuildRequires: gem(rails-dom-testing) >= 1
BuildConflicts: gem(mime-types) >= 4
BuildConflicts: gem(thor) >= 2.0
BuildConflicts: gem(rails-dom-testing) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mime-types >= 3.3.1,mime-types < 4
Requires:      gem(railties) >= 4.2.0
Requires:      gem(thor) >= 0.14
Requires:      gem(rails-dom-testing) >= 1
Conflicts:     gem(thor) >= 2.0
Conflicts:     gem(rails-dom-testing) >= 3
Provides:      gem(jquery-rails) = 4.5.0


%description
This gem provides jQuery and the jQuery-ujs driver for your Rails 4+
application.


%package       -n gem-jquery-rails-doc
Version:       4.5.0
Release:       alt1
Summary:       Use jQuery with Rails 4+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jquery-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jquery-rails) = 4.5.0

%description   -n gem-jquery-rails-doc
Use jQuery with Rails 4+ documentation files.

This gem provides jQuery and the jQuery-ujs driver for your Rails 4+
application.

%description   -n gem-jquery-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jquery-rails.


%package       -n gem-jquery-rails-devel
Version:       4.5.0
Release:       alt1
Summary:       Use jQuery with Rails 4+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jquery-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jquery-rails) = 4.5.0
Requires:      gem(rails) >= 0
Requires:      gem(rack) >= 0
Requires:      gem(json) >= 2
Requires:      gem(nokogiri) >= 0
Conflicts:     gem(mime-types) >= 4

%description   -n gem-jquery-rails-devel
Use jQuery with Rails 4+ development package.

This gem provides jQuery and the jQuery-ujs driver for your Rails 4+
application.

%description   -n gem-jquery-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jquery-rails.


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

%files         -n gem-jquery-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-jquery-rails-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 4.5.0-alt1
- ^ 4.4.0 -> 4.5.0

* Sun Sep 12 2021 Pavel Skrylev <majioa@altlinux.org> 4.4.0-alt1
- + packaged gem with Ruby Policy 2.0
