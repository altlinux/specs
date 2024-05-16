%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname irb

Name:          gem-irb
Epoch:         1
Version:       1.12.0
Release:       alt1
Summary:       Interactive Ruby command-line tool for REPL (Read Eval Print Loop)
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/irb
Vcs:           https://github.com/ruby/irb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(stackprof) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(tracer) >= 0
BuildRequires: gem(repl_type_completor) >= 0
BuildRequires: gem(reline) >= 0.4.2
BuildRequires: gem(rdoc) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(reline) >= 0.4.2
Requires:      gem(rdoc) >= 0
Provides:      gem(irb) = 1.12.0

%description
Interactive Ruby command-line tool for REPL (Read Eval Print Loop).


%package       -n irb
Version:       1.12.0
Release:       alt1
Summary:       Interactive Ruby command-line tool for REPL (Read Eval Print Loop) executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета irb
Group:         Other
BuildArch:     noarch

Requires(pre): alternatives >= 0:0.2.0-alt0.12
Requires:      gem(irb) = 1.12.0

%description   -n irb
Interactive Ruby command-line tool for REPL (Read Eval Print Loop)
executable(s).

%description   -n irb -l ru_RU.UTF-8
Исполнямка для самоцвета irb.


%if_enabled    doc
%package       -n gem-irb-doc
Version:       1.12.0
Release:       alt1
Summary:       Interactive Ruby command-line tool for REPL (Read Eval Print Loop) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета irb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(irb) = 1.12.0

%description   -n gem-irb-doc
Interactive Ruby command-line tool for REPL (Read Eval Print Loop) documentation
files.

%description   -n gem-irb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета irb.
%endif


%if_enabled    devel
%package       -n gem-irb-devel
Version:       1.12.0
Release:       alt1
Summary:       Interactive Ruby command-line tool for REPL (Read Eval Print Loop) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета irb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(irb) = 1.12.0
Requires:      gem(stackprof) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(tracer) >= 0
Requires:      gem(repl_type_completor) >= 0

%description   -n gem-irb-devel
Interactive Ruby command-line tool for REPL (Read Eval Print Loop) development
package.

%description   -n gem-irb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета irb.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

rm -rf %buildroot%_bindir/irb
mkdir -p %buildroot%_altdir/
cat <<EOF >>%buildroot%_altdir/irb
%{_bindir}/irb %ruby_gemlibdir/exe/irb 100
EOF

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n irb
%doc README.md
%_mandir/irb.1.xz
%_altdir/irb

%if_enabled    doc
%files         -n gem-irb-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-irb-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 1:1.12.0-alt1
- + packaged gem with Ruby Policy 2.0
