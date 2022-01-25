%define _unpackaged_files_terminate_build 1

%global _llvm_version 12.0

Name: llvm-common
Version: 12.0.0
Release: alt3

Summary: Common directories, symlinks and tool selection for LLVM
License: Apache-2.0 with LLVM-exception
Group: Development/Other
Url: http://git.altlinux.org/gears/l/llvm-common.git

Source: llvm-alt-tool-wrapper.c
Source1: alt-packaging-wrap-cmake-script
Source2: alt-packaging-produce-rpm-macros-llvm-common
Source3: llvm-common.env

# We want to have these obsoletions to win apt's generic provider selection
# against pre-wrapped llvm packages.
Obsoletes: clang              <= 11.0.0-alt1
Obsoletes: clang-devel        <= 11.0.0-alt1
Obsoletes: clang-devel-static <= 11.0.0-alt1
Obsoletes: clang-doc          <= 11.0.0-alt1
Obsoletes: lld                <= 11.0.0-alt1
Obsoletes: lld-devel          <= 11.0.0-alt1
Obsoletes: lld-doc            <= 11.0.0-alt1
Obsoletes: llvm               <= 11.0.0-alt1
Obsoletes: llvm-devel         <= 11.0.0-alt1
Obsoletes: llvm-devel-static  <= 11.0.0-alt1
Obsoletes: llvm-doc           <= 11.0.0-alt1

%define _libexecdir /usr/libexec

%package -n rpm-macros-%name
Summary: Default LLVM major branch and relevant RPM macros
License: Apache-2.0 with LLVM-exception
Group: System/Configuration/Packaging
BuildArch: noarch

%package -n llvm
Summary: Common symlinks for LLVM utilities
License: Apache-2.0 with LLVM-exception
Group: Development/C
BuildArch: noarch
Provides: llvm-common-util = %EVR
Requires: llvm%_llvm_version
Requires(pre,postun): %name = %version-%release

%package -n llvm-devel
Summary: Common symlinks and development files for LLVM utilities
License: Apache-2.0 with LLVM-exception
Group: Development/C
Provides: llvm-common-devel = %EVR
Requires: llvm%_llvm_version-devel
Requires(pre,postun): %name = %version-%release
Conflicts: llvm7.0-devel

%package -n llvm-devel-static
Summary: Common symlinks and development files for LLVM static libraries
License: Apache-2.0 with LLVM-exception
Group: Development/C
Provides: llvm-common-devel-static = %EVR
Requires: llvm%_llvm_version-devel-static
Requires(pre,postun): %name = %version-%release

%package -n clang
Summary: Common symlinks for Clang
License: Apache-2.0 with LLVM-exception
Group: Development/C
BuildArch: noarch
Provides: llvm-common-clang = %EVR
Requires: clang%_llvm_version
Requires(pre,postun): %name = %version-%release

%package -n clang-tools
Summary: Common symlink for Clang-based tools
License: Apache-2.0 with LLVM-exception
Group: Development/C
BuildArch: noarch
Provides: llvm-common-clang-tools = %EVR
Requires: clang%_llvm_version-tools
Requires(pre,postun): %name = %version-%release

%package -n clangd
Summary: Common symlinks for clangd, a Clang-based language server
License: Apache-2.0 with LLVM-exception
Group: Development/C
BuildArch: noarch
Provides: llvm-common-clangd = %EVR
Requires: clangd%_llvm_version
Requires(pre,postun): %name = %version-%release

%package -n clang-devel
Summary: Provides clang-devel
License: Apache-2.0 with LLVM-exception
Group: Development/C
Provides: llvm-common-clang-devel = %EVR
Requires: clang%_llvm_version-devel
Requires(pre,postun): %name = %version-%release

%package -n clang-devel-static
Summary: Provides clang-devel-static
License: Apache-2.0 with LLVM-exception
Group: Development/C
Provides: llvm-common-clang-devel-static = %EVR
Requires: clang%_llvm_version-devel-static
Requires(pre,postun): %name = %version-%release

%package -n lld
Summary: Common symlinks for lld
License: Apache-2.0 with LLVM-exception
Group: Development/Other
BuildArch: noarch
Provides: llvm-common-lld = %EVR
Requires: lld%_llvm_version
Requires(pre,postun): %name = %version-%release

%package -n lld-devel
Summary: Provides lld-devel and lld-devel-static
License: Apache-2.0 with LLVM-exception
Group: Development/Other
Provides: llvm-common-lld-devel = %EVR
Requires: lld%_llvm_version-devel
Requires(pre,postun): %name = %version-%release

%package -n lldb
Summary: Common symlinks for lldb
License: Apache-2.0 with LLVM-exception
Group: Development/Debuggers
BuildArch: noarch
Provides: llvm-common-lldb = %EVR
Requires: lldb%_llvm_version
Requires(pre,postun): %name = %version-%release

%package -n liblldb-devel
Summary: Provides lldb-devel
License: Apache-2.0 with LLVM-exception
Group: Development/Debuggers
BuildArch: noarch
Provides: llvm-common-liblldb-devel = %EVR
Requires: liblldb%_llvm_version-devel
Requires(pre,postun): %name = %version-%release

%description -n rpm-macros-%name
This package contains RPM macros related to LLVM packaging.

%description
This package contains common symlinks, directories and selection
utility for LLVM.

%description -n llvm
This package contains common symlinks to wrap various LLVM utilities.

%description -n llvm-devel
This package contains common development files and %_bindir/llvm-config.

%description -n llvm-devel-static
This package currently only pulls in the LLVM static libraries of the default
version.

%description -n clang
This package contains common symlinks to wrap Clang.

%description -n clang-tools
This package contains common symlinks to wrap the Clang-based tools.

%description -n clangd
This package contains common symlinks to wrap clangd, a Clang-based C and C++
language server.

%description -n clang-devel
This package contains clangXXX-devel and provides clang-devel.

%description -n clang-devel-static
This package contains clangXXX-devel-static and provides clang-devel-static.

%description -n lld
This package contains common symlinks to wrap LLD.

%description -n lld-devel
This package contains lldXXX-devel and provides lld-devel{,-static}.

%description -n lldb
This package contains common symlinks to wrap LLDB.

%description -n liblldb-devel
This package pulls in liblldbXXX-devel.

%prep
%setup -cT
%ifarch %e2k
%add_optflags -fwhole -g0
%else
%add_optflags -O3
%endif

%build
build_with()
{
"$1" %optflags -Werror \
	'-DPREFIX="%_prefix"' '-DLIBDIR="%_libdir"' '-DBINDIR="%_bindir"' \
	'-DPACKAGE_NAME="%name"' \
	'-DDEFAULT_VERSION="%_llvm_version"' \
	%_sourcedir/llvm-alt-tool-wrapper.c -o llvm-alt-tool-wrapper
}

# Directly access the C compiler (not via clang -> llvm-alt-tool-wrapper;
# in case of errors in the previous build of this package).
# Fall back to gcc to facilitate bootstrap builds.
%global __clang_versioned %_prefix/lib/llvm-%_llvm_version/bin/clang
for cc in %__clang_versioned %_prefix/lib/llvm-*/bin/clang %__cc; do
	build_with "$cc" && break
done

%install
mkdir -p %buildroot%_bindir/
install -p -m755 llvm-alt-tool-wrapper %buildroot%_bindir/

# Symlink tools to bindir.
# The tool list is obtained from package llvmYYY, where YYY is its major version.
%define install_tool_link() ln -s llvm-alt-tool-wrapper %buildroot%_bindir/%1
%install_tool_link bugpoint
%install_tool_link c-index-test
%install_tool_link clang++
%install_tool_link clang
%install_tool_link clang-apply-replacements
%install_tool_link clang-change-namespace
%install_tool_link clang-check
%install_tool_link clang-cl
%install_tool_link clang-cpp
%install_tool_link clang-doc
%install_tool_link clang-extdef-mapping
%install_tool_link clang-format
%install_tool_link clang-include-fixer
%install_tool_link clang-move
%install_tool_link clang-offload-bundler
%install_tool_link clang-offload-wrapper
%install_tool_link clang-query
%install_tool_link clang-refactor
%install_tool_link clang-rename
%install_tool_link clang-reorder-fields
%install_tool_link clang-scan-deps
%install_tool_link clang-tidy
%install_tool_link clangd
%install_tool_link diagtool
%install_tool_link dsymutil
%install_tool_link find-all-symbols
%install_tool_link git-clang-format
%install_tool_link hmaptool
%install_tool_link ld.lld
%install_tool_link ld64.lld
%install_tool_link llc
%install_tool_link lld
%install_tool_link lld-link
%install_tool_link lli
%install_tool_link llvm-addr2line
%install_tool_link llvm-ar
%install_tool_link llvm-as
%install_tool_link llvm-bcanalyzer
%install_tool_link llvm-c-test
%install_tool_link llvm-cat
%install_tool_link llvm-cfi-verify
%install_tool_link llvm-config
%install_tool_link llvm-cov
%install_tool_link llvm-cvtres
%install_tool_link llvm-cxxdump
%install_tool_link llvm-cxxfilt
%install_tool_link llvm-cxxmap
%install_tool_link llvm-diff
%install_tool_link llvm-dis
%install_tool_link llvm-dlltool
%install_tool_link llvm-dwarfdump
%install_tool_link llvm-dwp
%install_tool_link llvm-elfabi
%install_tool_link llvm-exegesis
%install_tool_link llvm-extract
%install_tool_link llvm-gsymutil
%install_tool_link llvm-ifs
%install_tool_link llvm-install-name-tool
%install_tool_link llvm-jitlink
%install_tool_link llvm-lib
%install_tool_link llvm-link
%install_tool_link llvm-lipo
%install_tool_link llvm-lto
%install_tool_link llvm-lto2
%install_tool_link llvm-mc
%install_tool_link llvm-mca
%install_tool_link llvm-ml
%install_tool_link llvm-modextract
%install_tool_link llvm-mt
%install_tool_link llvm-nm
%install_tool_link llvm-objcopy
%install_tool_link llvm-objdump
%install_tool_link llvm-opt-report
%install_tool_link llvm-pdbutil
%install_tool_link llvm-profdata
%install_tool_link llvm-ranlib
%install_tool_link llvm-rc
%install_tool_link llvm-readelf
%install_tool_link llvm-readobj
%install_tool_link llvm-reduce
%install_tool_link llvm-rtdyld
%install_tool_link llvm-size
%install_tool_link llvm-split
%install_tool_link llvm-stress
%install_tool_link llvm-strings
%install_tool_link llvm-strip
%install_tool_link llvm-symbolizer
%install_tool_link llvm-tblgen
%install_tool_link llvm-undname
%install_tool_link llvm-xray
%install_tool_link modularize
%install_tool_link obj2yaml
%install_tool_link opt
%install_tool_link pp-trace
%install_tool_link sancov
%install_tool_link sanstats
%install_tool_link scan-build
%install_tool_link scan-view
%install_tool_link verify-uselistorder
%install_tool_link wasm-ld
%install_tool_link yaml2obj

%install_tool_link lldb
%install_tool_link lldb-argdumper
%install_tool_link lldb-instr
%install_tool_link lldb-server
%install_tool_link lldb-vscode

# Wrap the CMake configs useful to external users to respect %%_llvm_version.
%define wrap_cmake_script() RPM_LLVM_VERSION=%_llvm_version %_sourcedir/alt-packaging-wrap-cmake-script %*
%wrap_cmake_script %_libdir/cmake/llvm/LLVMConfig.cmake
%wrap_cmake_script %_libdir/cmake/clang/ClangConfig.cmake

mkdir -p %buildroot%_rpmmacrosdir
RPM_LLVM_VERSION=%_llvm_version %_sourcedir/alt-packaging-produce-rpm-macros-llvm-common > %buildroot%_rpmmacrosdir/%name
cp %SOURCE3 %buildroot%_rpmmacrosdir/%name.env

%check
which %__clang_versioned || { echo 'Skipping the test of llvm-alt-tool-wrapper.'; exit 0; }
%{?_llvm_version:export ALTWRAP_LLVM_VERSION=%_llvm_version}
%buildroot%_bindir/llvm-alt-tool-wrapper --version && exit 1
%buildroot%_bindir/clang --version
%buildroot%_bindir/clang-cpp --version
%buildroot%_bindir/llc --version

%files -n rpm-macros-%name
%_rpmmacrosdir/%name
%_rpmmacrosdir/%name.env

%files
%_bindir/llvm-alt-tool-wrapper

%files -n llvm
%exclude %_bindir/llvm-alt-tool-wrapper
%_bindir/*
# llvm-common-devel
%exclude %_bindir/llvm-config
# llvm-common-clang{,d,-tools}
%exclude %_bindir/*clang*
# llvm-common-lld
%exclude %_bindir/*lld*
%exclude %_bindir/wasm-ld*

%files -n llvm-devel
%_bindir/llvm-config
%_libdir/cmake/llvm

%files -n llvm-devel-static

%files -n clang
%_bindir/clang++
%_bindir/clang
%_bindir/clang-cl
%_bindir/clang-cpp

%files -n clangd
%_bindir/clangd

%files -n clang-tools
%_bindir/*clang*
%exclude %_bindir/clang++
%exclude %_bindir/clang
%exclude %_bindir/clang-cl
%exclude %_bindir/clang-cpp
%exclude %_bindir/clangd

%files -n clang-devel
%_libdir/cmake/clang

%files -n clang-devel-static

%files -n lld
%_bindir/ld*.lld
%_bindir/lld
%_bindir/lld-link
%_bindir/wasm-ld

%files -n lld-devel

%files -n lldb
%_bindir/lldb
%_bindir/lldb-argdumper
%_bindir/lldb-instr
%_bindir/lldb-server
%_bindir/lldb-vscode

%package checkinstall
Summary: Installing me immediately runs the test for llvm-alt-tool-wrapper
Group: Development/C
BuildArch: noarch
Requires(pre,postun): %name = %EVR
# An error in llvm-alt-tool-wrapper can already be caught as an UNMET dependency.
Requires(pre,postun): %__clang_versioned

%description checkinstall
By installing this package, you immediately run the test
for llvm-alt-tool-wrapper.

%files checkinstall

%pre checkinstall
%{?_llvm_version:export ALTWRAP_LLVM_VERSION=%_llvm_version}
llvm-config --version
clang --version
clang-cpp --version
llc --version

%changelog
* Tue Jan 25 2022 Arseny Maslennikov <arseny@altlinux.org> 12.0.0-alt3
- llvm-common.env: Fixed extra quotes. (closes: 41796)

* Fri Aug 20 2021 Arseny Maslennikov <arseny@altlinux.org> 12.0.0-alt2
- Added %set_llvm_version.

* Wed Aug 11 2021 Arseny Maslennikov <arseny@altlinux.org> 12.0.0-alt1
- Made LLVM 12 the default.
- For each package in the llvm-common-* family, replaced it with its provide.
  The old name is retained as a provide for compatibility.

* Wed Aug 11 2021 Andrey Cherepanov <cas@altlinux.org> 11.0.1-alt3
- Added conflict with llvm7.0-devel.
- Fix bogus dates in %%changelog.

* Sun Feb 14 2021 Arseny Maslennikov <arseny@altlinux.org> 11.0.1-alt2
- Obsoleted the Sisyphus LLVM packages that do not use llvm-alt-tool-wrappers.

* Sat Jan 16 2021 Arseny Maslennikov <arseny@altlinux.org> 11.0.1-alt1
- Introduced wrappers for the following utilities:
  lldb
  lldb-argdumper
  lldb-instr
  lldb-server
  lldb-vscode
- Introduced liblldb-devel to pull in the default liblldbN-devel.

* Sun Jan 10 2021 Arseny Maslennikov <arseny@altlinux.org> 11.0.0-alt3
- Added new helper RPM macros for use in packaging of LLVM/Clang-reliant
  software.

* Sun Nov 22 2020 Arseny Maslennikov <arseny@altlinux.org> 11.0.0-alt2
- Specified requirements for llvm%%_llvm_version in the -common packages.
- Introduced wrappers for clang-tools-extra and clangd.
- Introduced llvm-common-devel-static to provide llvm-devel-static.

* Sun Nov 08 2020 Arseny Maslennikov <arseny@altlinux.org> 11.0.0-alt1
- Initial revision.
