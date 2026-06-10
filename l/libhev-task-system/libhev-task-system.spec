Name:           libhev-task-system
Version:        5.10.2
Release:        alt1
Source:         hev-task-system-%version.tar.gz

Summary:        A simple, lightweight multi-task system (coroutines)
License:        MIT
Group:          Development/C
URL:            https://hev.cc/
VCS:            https://github.com/heiher/hev-task-system

# Automatically added by buildreq on Mon Jun 08 2026
# optimized out: at-spi2-atk bash5 glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgcc15-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libharfbuzz-devel libp11-kit libpango-devel libsasl2-3 libwayland-client libwayland-cursor libwayland-egl pkg-config python3 python3-base sh5 zlib-devel
BuildRequires: libcurl-devel libgtk+3-devel

%description
The task system is executed within a native process/thread. In task
system, you can create many tasks and attach them to the task system.
When a task yields or is blocked by I/O, the scheduler will pick
a suitable task from running list and switch to it. Memory space, file
descriptors, and other resources are shared among all tasks in the task
system. Each task has its private, standalone task structure (#HevTask)
and stack in heap of the process.

Within a task, you can allocate memory from heap, read and write data to
the stack, and perform I/O operations in synchronized mode.

%package devel
Summary:        Development version of %name
Group:          Development/C
%description devel
%summary

%package demos
Summary:        Demo applications for %name
Group:          Development/C
%description demos
%summary

%prep
%setup -n hev-task-system-%version
sed -i '/@printf/d' Makefile

%build
%make_build CFLAGS="%optflags" LFLAGS="-Wl,-soname,%name.so.0" shared apps

%install
install -D bin/%name.so %buildroot%_libdir/%name.so.0
ln -sr %buildroot%_libdir/%name.so.0 %buildroot%_libdir/%name.so
mkdir -p %buildroot%_includedir
install -m644 include/* %buildroot%_includedir/
mkdir -p %buildroot%_libdir/hev-task-system-demos
install bin/[^l]* %buildroot%_libdir/hev-task-system-demos/

%files
%doc README*
%_libdir/%name.so.0

%files devel
%_libdir/%name.so
%_includedir/hev-*

%files demos
%_libdir/hev-task-system-demos

%changelog
* Mon Jun 08 2026 Fr. Br. George <george@altlinux.org> 5.10.2-alt1
- Initial build for ALT
