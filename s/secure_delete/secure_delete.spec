# SPEC-file for secure_delete
#

Name: secure_delete
Version: 3.1
Release: alt5

Summary: Utilities for secure deleting data
Summary(ru_RU.UTF-8): Утилиты для надёжного удаления данных

License: %gpl2only
Group: System/Base
URL: https://www.thc.org/

Source0: %name-%version.tar
Patch0:  %name-3.1-kernel_module-alt.patch
Patch1:  %name-3.1-configure-rand-file.patch
Patch2:  debian-gcc-15.patch
Patch3:  secure_delete-3.1-alt-sdel_add_missing_byte_for_NULL_terminator.patch
Patch4:  secure_delete-3.1-alt-sdel_fix_memory_leak_of_template.patch
Patch5:  secure_delete-3.1-alt-sdel_eliminate_dead_code.patch
Patch6:  secure_delete-3.1-alt-sdel_fix_off_by_one_read.patch
Patch7:  secure_delete-3.1-alt-sdel_fix_warning_report_condition.patch
Patch8:  secure_delete-3.1-alt-sdel_prevent_NULL_dereference_on_allocation_failure.patch
Patch9:  secure_delete-3.1-alt-srm_fix_file_descriptor_leak.patch
Patch10:  secure_delete-3.1-alt-sfill_split_path_handling_into_dir_and_tmppath_variables.patch
Patch11:  secure_delete-3.1-alt-sfill_replace_VLA_with_fixed_PATH_MAX_buffer_built_via_snprintf.patch
Patch12:  secure_delete-3.1-alt-sfill_fix_directory_descriptor_leak.patch

BuildRequires(pre): rpm-build-licenses

Conflicts: srm

%description
THC Secure Delete is a set  of four utilities to perform the
following:  secure deletion of files,  secure overwriting of
the unused diskspace on the harddisk, secure overwriting and
cleaning of the swap filesystem  and secure overwriting  and
cleaning of the unused memory.

%description -l ru_RU.UTF-8
THC Secure Delete - набор четырёх утилит  для безопасного
удаления  файлов,  безопасной очистки  от остатков данных
неиспользуемого  пространства дисков,  безопасной очистки
разделов подкачки  и  безопасной  очистки  неиспользуемой
памяти.

%prep
%setup
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p2
%patch5 -p2
%patch6 -p2
%patch7 -p2
%patch8 -p2
%patch9 -p2
%patch10 -p2
%patch11 -p2
%patch12 -p2

%build
make sdel-lib.o srm sfill sswap smem

%install
mkdir -p -- %buildroot%_bindir
mkdir -p -- %buildroot%_man1dir

cp -- srm sfill smem sswap %buildroot%_bindir
cp -- srm.1 sfill.1 smem.1 sswap.1 %buildroot%_man1dir

%files
%doc CHANGES README usenix6-gutmann.doc secure_delete.doc the_cleaner.sh
%_bindir/sfill
%_bindir/smem
%_bindir/srm
%_bindir/sswap
%_man1dir/srm.1.*
%_man1dir/sfill.1.*
%_man1dir/smem.1.*
%_man1dir/sswap.1.*

%changelog
* Mon Oct 12 2026 Sergey Zhidkih <rx1513@altlinux.org> 3.1-alt5
- Fix several memory and descriptor leaks, OOB read and write.
- Fix warning message for sdel.

* Sat Aug 01 2026 Anton Midyukov <antohami@altlinux.org> 3.1-alt4
- Fix FTBFS with gcc15.

* Mon Jul 19 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.1-alt3
- Add the configure-rand-file patch from C7.1

* Mon Jul 19 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.1-alt2
- Add conflict on srm package (Closes: 36753)
- Spec file cleanup

* Mon Sep 5 2005 Nikolay A. Fetisov <naf@altlinux.ru> 3.1-alt1
- Initial build for ALTLinux Sisyphus

* Thu Aug 11 2005 Nikolay A. Fetisov <naf@altlinux.ru> 3.1-alt0
- Initial build

