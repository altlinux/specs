%define        gemname rdoc

Name:          gem-rdoc
Version:       6.4.0
Release:       alt1
Summary:       RDoc produces HTML and online documentation for Ruby projects
License:       Ruby
Group:         Development/Ruby
Url:           https://ruby.github.io/rdoc/
Vcs:           https://github.com/ruby/rdoc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(psych) >= 4.0.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(psych) >= 4.0.0
Obsoletes:     ruby-rdoc < %EVR
Provides:      ruby-rdoc = %EVR
Provides:      gem(rdoc) = 6.4.0

%description
RDoc produces HTML and online documentation for Ruby projects. RDoc includes the
rdoc and ri tools for generating and displaying online documentation.


%package       -n rdoc
Version:       6.4.0
Release:       alt1
Summary:       RDoc produces HTML and online documentation for Ruby projects executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rdoc
Group:         Other
BuildArch:     noarch

Requires:      gem(rdoc) = 6.4.0
Obsoletes:     ruby-tool-rdoc
Obsoletes:     ruby-tools
Conflicts:     rdoc <= 1.9.3-alt10

%description   -n rdoc
RDoc produces HTML and online documentation for Ruby projects
executable(s).

RDoc produces HTML and online documentation for Ruby projects. RDoc includes the
rdoc and ri tools for generating and displaying online documentation.

%description   -n rdoc -l ru_RU.UTF-8
Исполнямка для самоцвета rdoc.


%package       -n ri
Version:       6.4.0
Release:       alt1
Summary:       RI produces HTML and online documentation for Ruby projects executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rdoc
Group:         Other
BuildArch:     noarch

Requires:      gem(rdoc) = 6.4.0

%description   -n ri
RDoc produces HTML and online documentation for Ruby projects
executable(s).

RDoc produces HTML and online documentation for Ruby projects. RDoc includes the
rdoc and ri tools for generating and displaying online documentation.

%description   -n ri -l ru_RU.UTF-8
Исполнямка для самоцвета rdoc.


%package       -n gem-rdoc-doc
Version:       6.4.0
Release:       alt1
Summary:       RDoc produces HTML and online documentation for Ruby projects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rdoc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rdoc) = 6.4.0

%description   -n gem-rdoc-doc
RDoc produces HTML and online documentation for Ruby projects documentation
files.

RDoc produces HTML and online documentation for Ruby projects. RDoc includes the
rdoc and ri tools for generating and displaying online documentation.

%description   -n gem-rdoc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rdoc.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n rdoc
%doc README.rdoc
%_bindir/rdoc

%files         -n ri
%doc README.rdoc
%_bindir/ri
%_mandir/ri*

%files         -n gem-rdoc-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Sat May 14 2022 Pavel Skrylev <majioa@altlinux.org> 6.4.0-alt1
- ^ 6.3.0 -> 6.4.0

* Wed Apr 28 2021 Pavel Skrylev <majioa@altlinux.org> 6.3.0-alt1
- ^ 6.1.1 -> 6.3.0

* Fri Mar 08 2019 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt3
- > Ruby Policy 2.0

* Fri Jan 18 2019 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt2
- + lost provides ruby-tool-rdoc
- * Minor change in rspec

* Tue Jan 15 2019 Pavel Skrylev <majioa@altlinux.org> 6.1.1-alt1
- Initial build for Sisyphus, packaged as a gem
