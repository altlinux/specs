%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname path_expander

Name:          gem-path-expander
Version:       2.0.1
Release:       alt1
Summary:       PathExpander helps pre-process command-line arguments expanding directories into their constituent files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/path_expander
Vcs:           https://github.com/seattlerb/path_expander.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 0
BuildRequires: gem(rdoc) >= 4.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names path_expander,path-expander
%ruby_ignore_names _names
Provides:      path_expander = %EVR
Provides:      gem(path_expander) = 2.0.1

%description
PathExpander helps pre-process command-line arguments expanding directories into
their constituent files. It further helps by providing additional mechanisms to
make specifying subsets easier with path subtraction and allowing for
command-line arguments to be saved in a file.

NOTE: this is NOT an options processor. It is a path processor (basically
everything else besides options). It does provide a mechanism for pre-filtering
cmdline options, but not with the intent of actually processing them in
PathExpander. Use OptionParser to deal with options either before or after
passing ARGV through PathExpander.


%if_enabled    doc
%package       -n gem-path-expander-doc
Version:       2.0.1
Release:       alt1
Summary:       PathExpander helps pre-process command-line arguments expanding directories into their constituent files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета path_expander
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(path_expander) = 2.0.1

%description   -n gem-path-expander-doc
PathExpander helps pre-process command-line arguments expanding directories into
their constituent files documentation files.

PathExpander helps pre-process command-line arguments expanding directories into
their constituent files. It further helps by providing additional mechanisms to
make specifying subsets easier with path subtraction and allowing for
command-line arguments to be saved in a file.

NOTE: this is NOT an options processor. It is a path processor (basically
everything else besides options). It does provide a mechanism for pre-filtering
cmdline options, but not with the intent of actually processing them in
PathExpander. Use OptionParser to deal with options either before or after
passing ARGV through PathExpander.

%description   -n gem-path-expander-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета path_expander.
%endif


%if_enabled    devel
%package       -n gem-path-expander-devel
Version:       2.0.1
Release:       alt1
Summary:       PathExpander helps pre-process command-line arguments expanding directories into their constituent files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета path_expander
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(path_expander) = 2.0.1
Requires:      gem(hoe) >= 0
Requires:      gem(rdoc) >= 4.0

%description   -n gem-path-expander-devel
PathExpander helps pre-process command-line arguments expanding directories into
their constituent files development package.

PathExpander helps pre-process command-line arguments expanding directories into
their constituent files. It further helps by providing additional mechanisms to
make specifying subsets easier with path subtraction and allowing for
command-line arguments to be saved in a file.

NOTE: this is NOT an options processor. It is a path processor (basically
everything else besides options). It does provide a mechanism for pre-filtering
cmdline options, but not with the intent of actually processing them in
PathExpander. Use OptionParser to deal with options either before or after
passing ARGV through PathExpander.

%description   -n gem-path-expander-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета path_expander.
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
%doc History.rdoc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-path-expander-doc
%doc History.rdoc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-path-expander-devel
%doc History.rdoc README.rdoc
%endif


%changelog
* Mon Aug 31 2026 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- ^ 1.1.3 -> 2.0.1

* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- ^ 1.1.0 -> 1.1.3

* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
