%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname activeresource

Name:          gem-activeresource
Version:       6.1.0
Release:       alt1
Summary:       REST modeling framework (part of Rails)
License:       MIT
Group:         Development/Ruby
Url:           http://www.rubyonrails.org
Vcs:           https://github.com/rails/activeresource/tree/v6.1.0.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(rubocop-packaging) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rails) >= 0
BuildRequires: gem(minitest-bisect) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(mocha) >= 0.13.0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(activesupport) >= 6.0
BuildRequires: gem(activemodel) >= 6.0
BuildRequires: gem(activemodel-serializers-xml) >= 1.0
BuildConflicts: gem(activemodel-serializers-xml) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activesupport) >= 6.0
Requires:      gem(activemodel) >= 6.0
Requires:      gem(activemodel-serializers-xml) >= 1.0
Conflicts:     gem(activemodel-serializers-xml) >= 2
Provides:      gem(activeresource) = 6.1.0


%description
REST on Rails. Wrap your RESTful web app with Ruby classes and work with them
like Active Record models.


%if_enabled    doc
%package       -n gem-activeresource-doc
Version:       6.1.0
Release:       alt1
Summary:       REST modeling framework (part of Rails) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activeresource
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activeresource) = 6.1.0

%description   -n gem-activeresource-doc
REST modeling framework (part of Rails) documentation files.

REST on Rails. Wrap your RESTful web app with Ruby classes and work with them
like Active Record models.

%description   -n gem-activeresource-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activeresource.
%endif


%if_enabled    devel
%package       -n gem-activeresource-devel
Version:       6.1.0
Release:       alt1
Summary:       REST modeling framework (part of Rails) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activeresource
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activeresource) = 6.1.0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-minitest) >= 0
Requires:      gem(rubocop-packaging) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rails) >= 0
Requires:      gem(minitest-bisect) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(mocha) >= 0.13.0
Requires:      gem(rexml) >= 0
Requires:      gem(ruby-prof) >= 0

%description   -n gem-activeresource-devel
REST modeling framework (part of Rails) development package.

REST on Rails. Wrap your RESTful web app with Ruby classes and work with them
like Active Record models.

%description   -n gem-activeresource-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activeresource.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-activeresource-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-activeresource-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 6.1.0-alt1
- + packaged gem with Ruby Policy 2.0
