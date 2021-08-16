%define        gemname pry-doc

Name:          gem-pry-doc
Version:       1.1.0
Release:       alt1
Summary:       Provides YARD and extended documentation support for Pry
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pry/pry-doc
Vcs:           https://github.com/pry/pry-doc.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         etags.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(yard) >= 0.9.11 gem(yard) < 0.10
BuildRequires: gem(latest_ruby) >= 2.0 gem(latest_ruby) < 4
BuildRequires: gem(rspec) >= 3.5 gem(rspec) < 4
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: /usr/bin/etags

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency latest_ruby >= 3.0.1,latest_ruby < 4
Requires:      gem(yard) >= 0.9.11 gem(yard) < 0.10
Requires:      gem(pry) >= 0.11 gem(pry) < 1
Requires:      /usr/bin/etags
Provides:      gem(pry-doc) = 1.1.0


%description
Pry Doc is a Pry REPL plugin. It provides extended documentation support for the
REPL by means of improving the `show-doc` and `show-source` commands. With help
of the plugin the commands are be able to display the source code and the docs
of Ruby methods and classes implemented in C. documentation


%package       -n gem-pry-doc-doc
Version:       1.1.0
Release:       alt1
Summary:       Provides YARD and extended documentation support for Pry documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pry-doc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pry-doc) = 1.1.0

%description   -n gem-pry-doc-doc
Provides YARD and extended documentation support for Pry documentation
files.

Pry Doc is a Pry REPL plugin. It provides extended documentation support for the
REPL by means of improving the `show-doc` and `show-source` commands. With help
of the plugin the commands are be able to display the source code and the docs
of Ruby methods and classes implemented in C. documentation

%description   -n gem-pry-doc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pry-doc.


%package       -n gem-pry-doc-devel
Version:       1.1.0
Release:       alt1
Summary:       Provides YARD and extended documentation support for Pry development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pry-doc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pry-doc) = 1.1.0
Requires:      gem(latest_ruby) >= 2.0 gem(latest_ruby) < 4
Requires:      gem(rspec) >= 3.5 gem(rspec) < 4
Requires:      gem(rake) >= 10.0 gem(rake) < 14

%description   -n gem-pry-doc-devel
Provides YARD and extended documentation support for Pry development
package.

Pry Doc is a Pry REPL plugin. It provides extended documentation support for the
REPL by means of improving the `show-doc` and `show-source` commands. With help
of the plugin the commands are be able to display the source code and the docs
of Ruby methods and classes implemented in C. documentation

%description   -n gem-pry-doc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pry-doc.


%prep
%setup
%patch
rm -rf libexec

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

%files         -n gem-pry-doc-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-pry-doc-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
