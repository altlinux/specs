%define        gemname therubyrhino

Name:          gem-therubyrhino
Version:       2.0.4
Release:       alt1
Summary:       Embed the Rhino JavaScript interpreter into JRuby
License:       MPL-2.0 or MIT
Group:         Development/Ruby
Url:           http://github.com/cowboyd/therubyrhino
Vcs:           https://github.com/cowboyd/therubyrhino.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 2.14.1
BuildRequires: gem(mocha) >= 0.13.3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(mocha) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(therubyrhino_jar) >= 1.7.3
Provides:      gem(therubyrhino) = 2.0.4


%description
Call javascript code and manipulate javascript objects from ruby. Call ruby code
and manipulate ruby objects from javascript.


%package       -n gem-therubyrhino-jar
Version:       1.7.4
Release:       alt1
Summary:       Rhino's jars packed for therubyrhino
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(therubyrhino_jar) = 1.7.4

%description   -n gem-therubyrhino-jar
Rhino's js.jar classes packaged as a JRuby gem.


%package       -n gem-therubyrhino-jar-doc
Version:       1.7.4
Release:       alt1
Summary:       Rhino's jars packed for therubyrhino documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета therubyrhino_jar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(therubyrhino_jar) = 1.7.4

%description   -n gem-therubyrhino-jar-doc
Rhino's jars packed for therubyrhino documentation files.

Rhino's js.jar classes packaged as a JRuby gem.

%description   -n gem-therubyrhino-jar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета therubyrhino_jar.


%package       -n gem-therubyrhino-jar-devel
Version:       1.7.4
Release:       alt1
Summary:       Rhino's jars packed for therubyrhino development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета therubyrhino_jar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(therubyrhino_jar) = 1.7.4

%description   -n gem-therubyrhino-jar-devel
Rhino's jars packed for therubyrhino development package.

Rhino's js.jar classes packaged as a JRuby gem.

%description   -n gem-therubyrhino-jar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета therubyrhino_jar.


%package       -n gem-therubyrhino-doc
Version:       2.0.4
Release:       alt1
Summary:       Embed the Rhino JavaScript interpreter into JRuby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета therubyrhino
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(therubyrhino) = 2.0.4

%description   -n gem-therubyrhino-doc
Embed the Rhino JavaScript interpreter into JRuby documentation files.

Call javascript code and manipulate javascript objects from ruby. Call ruby code
and manipulate ruby objects from javascript.

%description   -n gem-therubyrhino-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета therubyrhino.


%package       -n gem-therubyrhino-devel
Version:       2.0.4
Release:       alt1
Summary:       Embed the Rhino JavaScript interpreter into JRuby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета therubyrhino
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(therubyrhino) = 2.0.4
Requires:      gem(rspec) >= 2.14.1
Requires:      gem(mocha) >= 0.13.3
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(mocha) >= 2

%description   -n gem-therubyrhino-devel
Embed the Rhino JavaScript interpreter into JRuby development package.

Call javascript code and manipulate javascript objects from ruby. Call ruby code
and manipulate ruby objects from javascript.

%description   -n gem-therubyrhino-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета therubyrhino.


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

%files         -n gem-therubyrhino-jar
%ruby_gemspecdir/therubyrhino_jar-1.7.4.gemspec
%ruby_gemslibdir/therubyrhino_jar-1.7.4

%files         -n gem-therubyrhino-jar-doc
%ruby_gemsdocdir/therubyrhino_jar-1.7.4

%files         -n gem-therubyrhino-jar-devel

%files         -n gem-therubyrhino-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-therubyrhino-devel
%doc README.md


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 2.0.4-alt1
- + packaged gem with Ruby Policy 2.0
