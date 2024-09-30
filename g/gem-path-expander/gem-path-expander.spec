%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname path_expander

Name:          gem-path-expander
Version:       1.1.3
Release:       alt1
Summary:       PathExpander helps pre-process command-line arguments expanding directories into their constituent files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/path_expander
Vcs:           https://github.com/seattlerb/path_expander.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 4.2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(hoe) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_alias_names path_expander,path-expander
%ruby_ignore_names cgi_multipart_eof_fix,gem_plugin,(?-mix:mongrel_),fastthread,(?-mix:project)
Provides:      gem(path_expander) = 1.1.3


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
Version:       1.1.3
Release:       alt1
Summary:       PathExpander helps pre-process command-line arguments expanding directories into their constituent files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета path_expander
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(path_expander) = 1.1.3

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
Version:       1.1.3
Release:       alt1
Summary:       PathExpander helps pre-process command-line arguments expanding directories into their constituent files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета path_expander
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(path_expander) = 1.1.3
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 4.2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-path-expander-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-path-expander-devel
%doc README.rdoc
%endif


%changelog
* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- ^ 1.1.0 -> 1.1.3

* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
