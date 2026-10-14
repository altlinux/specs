%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
# eu-elflint does not understand Go-specific ELF notes and sections in cftool.
%set_verify_elf_method strict,lint=relaxed

Name: retrowrite
Version: 0.0.0
Release: alt1.git3b1e366f

Summary: Static binary rewriting framework
Summary(ru_RU.UTF-8): Фреймворк статического переписывания бинарных файлов
License: MIT
Group: Development/Tools
Url: https://github.com/HexHive/retrowrite
Vcs: https://github.com/HexHive/retrowrite.git
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Patch0: %name-%version-alt-python3-compat.patch
Patch1: %name-%version-alt-replace-archinfo.patch
Patch2: %name-%version-alt-fix-x64-imports.patch
Patch3: %name-%version-alt-installed-paths.patch
Patch4: %name-%version-alt-cftool-go-module.patch

Requires: gcc-c++
Requires: python3-module-capstone
Requires: python3-module-elftools
Requires: python3-module-intervaltree

BuildRequires(pre): rpm-build-golang rpm-build-python3
BuildRequires: gcc
BuildRequires: python3-module-capstone python3-module-elftools python3-module-intervaltree

%description
RetroWrite is a static binary rewriting framework for x86-64 and AArch64.
It uses reassemblable assembly to add instrumentation to binaries without
requiring their source code.

%description -l ru_RU.UTF-8
RetroWrite — фреймворк статического переписывания бинарных файлов для x86-64
и AArch64. Он использует повторно собираемый ассемблерный код для добавления
инструментирования без доступа к исходному коду обрабатываемых программ.

%prep
%setup
%autopatch -p1

%build
go -C librw_x64/cftool build -buildmode=pie -o ../../cftool .

%install
install -d %buildroot%_bindir
install -d %buildroot%_libexecdir/%name
install -d %buildroot%_datadir/%name
install -d %buildroot%python3_sitelibdir_noarch
install -pm0755 retrowrite %buildroot%_bindir/%name
install -pm0755 cftool %buildroot%_libexecdir/%name/cftool
install -pm0644 rwtools_arm64/data_in_text/segfault_handler.s %buildroot%_datadir/%name/segfault_handler.s
install -pm0644 retrowrite_arch.py %buildroot%python3_sitelibdir_noarch/retrowrite_arch.py
cp -a librw_arm64 librw_x64 rwtools_arm64 rwtools_x64 %buildroot%python3_sitelibdir_noarch/
rm -rf %buildroot%python3_sitelibdir_noarch/librw_arm64/tests \
       %buildroot%python3_sitelibdir_noarch/librw_x64/cftool \
       %buildroot%python3_sitelibdir_noarch/rwtools_arm64/data_in_text
find %buildroot%python3_sitelibdir_noarch -type d -name __pycache__ -exec rm -rf '{}' +

%check
python3 -m compileall -q retrowrite_arch.py retrowrite librw_arm64 librw_x64 rwtools_arm64 rwtools_x64
PYTHONPATH=. python3 -c 'from retrowrite_arch import ArchAMD64, ArchAArch64; from librw_x64.analysis.register import RegisterAnalysis; from rwtools_x64.kasan.instrument import Instrument; from rwtools_x64.kcov.instrument import Instrument as KcovInstrument; assert ArchAMD64().register_list; assert ArchAArch64().register_list'
PYTHONPATH=. ./retrowrite --help >/dev/null
printf '{}\n' > cftool-input.json
./cftool cftool-input.json cftool-output.json
grep -qx '{}' cftool-output.json

%files
%doc LICENSE README.md
%_bindir/%name
%_libexecdir/%name/
%_datadir/%name/
%python3_sitelibdir_noarch/retrowrite_arch.py
%python3_sitelibdir_noarch/__pycache__/retrowrite_arch.*
%python3_sitelibdir_noarch/librw_arm64/
%python3_sitelibdir_noarch/librw_x64/
%python3_sitelibdir_noarch/rwtools_arm64/
%python3_sitelibdir_noarch/rwtools_x64/

%changelog
* Mon Oct 05 2026 Georgij Tsarin <crystarm@altlinux.org> 0.0.0-alt1.git3b1e366f
- Initial build for Sisyphus.
