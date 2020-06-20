#%global debug_package %{nil}

Name:    ck
Version: 0.6.0
Release: 1
Summary: Concurrency programming lib
License: BSD
URL:	 http://concurrencykit.org/
Source0: http://concurrencykit.org/releases/%{name}-%{version}.tar.gz

BuildRequires: 	gcc autoconf automake 

%description
Concurrency primitives, safe memory reclamation mechanisms and non-blocking data structures for the research, design and implementation of high performance concurrent systems. 

%package devel
Summary: Concurrency programming devel package
Requires: %{name} = %{version}-%{release}

%description devel
Concurrency primitives, safe memory reclamation mechanisms and non-blocking data structures for the research, design and implementation of high performance concurrent systems. 



%prep
%setup -q -n %{name}-%{version}/

%build
./configure --libdir=%{_libdir} --includedir=%{_includedir}/%{name} --mandir=%{_mandir} --prefix=%{_prefix}
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libck.a

%pre
%preun
%post
%postun

%check

%files
%license LICENSE 
%doc README 
%{_libdir}/libck.so.*

%files devel
%{_includedir}/*
%{_libdir}/libck.so
%{_mandir}/*
%{_libdir}/pkgconfig/*

%ldconfig_scriptlets

%changelog
* Sun Mar 29 2020 Wei Xiong <myeuler@163.com>
- Package init

