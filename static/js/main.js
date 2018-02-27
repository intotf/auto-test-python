$(function () {
  /*
  //点击删除弹出提示框时确认操作
  $(document).on('click', '.popover-content .label-warning', function () {
    $(this).parentsUntil('tbody').slideUp(function () {
      $(this).remove()
    })
  })

  //点击删除弹出提示框时取消操作
  $(document).on('click', '.popover-content .label-info', function () {
    $(this).parentsUntil('td').popover('hide')
  })

  $('[data-toggle="popover"]').popover({
    selector: '.fa-trash-o',
    html: true,
    content: '<span class="label label-warning"><i class="fa fa-check" @click="greet"></i> 是</span> <span class="label label-info"><i class="fa fa-times"></i> 否</span>'
  })
  */

  //select2
  try {
    $('.js-select2').select2()
  } catch (e) {

  }
})