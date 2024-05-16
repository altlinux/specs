%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rdoc

Name:          gem-rdoc
Version:       6.6.3.1
Release:       alt1.1
Summary:       RDoc produces HTML and online documentation for Ruby projects
License:       Ruby
Group:         Development/Ruby
Url:           https://ruby.github.io/rdoc/
Vcs:           https://github.com/ruby/rdoc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         use_system_dirs.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(kpeg) >= 1.3.3
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(racc) > 1.4.10
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(gettext) >= 0
BuildRequires: gem(psych) >= 4.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(psych) >= 4.0.0
Obsoletes:     ruby-rdoc < %EVR
Provides:      ruby-rdoc = %EVR
Provides:      gem(rdoc) = 6.6.3.1

%ruby_on_build_rake_tasks generate

%description
RDoc produces HTML and online documentation for Ruby projects. RDoc includes the
rdoc and ri tools for generating and displaying online documentation.


%package       -n rdoc
Version:       6.6.3.1
Release:       alt1.1
Summary:       RDoc produces HTML and online documentation for Ruby projects executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rdoc
Group:         Other
BuildArch:     noarch

Requires(pre): alternatives >= 0:0.2.0-alt0.12
Requires:      gem(rdoc) = 6.6.3.1
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
Version:       6.6.3.1
Release:       alt1.1
Summary:       RDoc produces HTML and online documentation for Ruby projects executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rdoc
Group:         Other
BuildArch:     noarch

Requires(pre): alternatives >= 0:0.2.0-alt0.12
Requires:      gem(rdoc) = 6.6.3.1

%description   -n ri
RDoc produces HTML and online documentation for Ruby projects
executable(s).

RDoc produces HTML and online documentation for Ruby projects. RDoc includes the
rdoc and ri tools for generating and displaying online documentation.
%description   -n ri -l ru_RU.UTF-8
Исполнямка для самоцвета rdoc.


%if_enabled    doc
%package       -n gem-rdoc-doc
Version:       6.6.3.1
Release:       alt1.1
Summary:       RDoc produces HTML and online documentation for Ruby projects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rdoc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rdoc) = 6.6.3.1

%description   -n gem-rdoc-doc
RDoc produces HTML and online documentation for Ruby projects documentation
files.

RDoc produces HTML and online documentation for Ruby projects. RDoc includes the
rdoc and ri tools for generating and displaying online documentation.
%description   -n gem-rdoc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rdoc.
%endif


%if_enabled    devel
%package       -n gem-rdoc-devel
Version:       6.6.3.1
Release:       alt1.1
Summary:       RDoc produces HTML and online documentation for Ruby projects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rdoc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rdoc) = 6.6.3.1
Requires:      gem(rake) >= 0
Requires:      gem(racc) > 1.4.10
Requires:      gem(kpeg) >= 1.3.3
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(gettext) >= 0

%description   -n gem-rdoc-devel
RDoc produces HTML and online documentation for Ruby projects development
package.

RDoc produces HTML and online documentation for Ruby projects. RDoc includes the
rdoc and ri tools for generating and displaying online documentation.
%description   -n gem-rdoc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rdoc.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

rm -rf %buildroot%_bindir/*
mkdir -p %buildroot%_altdir/
cat <<EOF >>%buildroot%_altdir/ri
%{_bindir}/ri %ruby_gemlibdir/exe/ri 100
EOF
cat <<EOF >>%buildroot%_altdir/rdoc
%{_bindir}/rdoc %ruby_gemlibdir/exe/rdoc 100
EOF

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n rdoc
%doc README.rdoc
%_altdir/rdoc

%files         -n ri
%doc README.rdoc
%_altdir/ri
%_mandir/ri*

%if_enabled    doc
%files         -n gem-rdoc-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rdoc-devel
%doc README.rdoc
%endif


%changelog
* Sun Apr 21 2024 Pavel Skrylev <majioa@altlinux.org> 6.6.3.1-alt1.1
- + added executables alternatives for ri, rdoc

* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 6.6.3.1-alt1
- ^ 6.6.2 -> 6.6.3.1
- ! fixed use system dirs feature

* Sun Feb 04 2024 Pavel Skrylev <majioa@altlinux.org> 6.6.2-alt1.1
- ! fixed build with compilation markdown rb (closes #49288)

* Sat Feb 03 2024 Pavel Skrylev <majioa@altlinux.org> 6.6.2-alt1
- ^ 6.4.0[1] -> 6.6.2

* Mon Jul 11 2022 Pavel Skrylev <majioa@altlinux.org> 6.4.0.1-alt1
- ^ 6.4.0 -> 6.4.0[1]
- ! paths to ri system folder
- ! dep to kpeg

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
